.. code-block:: php

    $db = & DB :: connect('mysql://' . $db_user . ':' . $db_pass . '@' . $db_host . '/' . $db_name, $options);
    helper::initialDBSettings($db);
    if (PEAR :: isError($db))
        die($db->getMessage());
    $db->setFetchMode(DB_FETCHMODE_ASSOC);

    // Mercator Meter
    $actual_data_last = false;
    if (strlen($asset_id)) {
        $masset_id = ' AND m.ID IN (' . $asset_id . ')';
        $asset_id = ' AND l.Asset_ID IN (' . $asset_id . ')';
    }
    $sSettingExtension = ($_SESSION['user_mandant_type']=='SUPER') ? $_SESSION['user_mandant'].'_' : '';
    $sJson = $db->getOne("SELECT value FROM users_setting WHERE UserID=".$_SESSION['user_id']." AND Name='{$sSettingExtension}overview'");
    if($sJson{0}!='{') {
        //1:2|118|121|119|122|120|1|5:Transport
        $aSettings = explode(":", $sJson);
        $sJson = json_encode((object) array('fleet'=>explode('|', $aSettings[0]), 'unit'=>explode('|', $aSettings[1]), 'tab'=>$aSettings[2]));
    }
    $oJson = json_decode($sJson, true);

    $sNameColumn = "m.`Name`";
    if($oJson['firstcolumn']=='transport') {
        $sNameColumn = 'IF(m.TransportName IS NOT NULL AND m.TransportName<>"", m.TransportName, m.`Name`) AS Name';
    }
    // error_log("XXX");

    $waittime = time()+60;
    do {
        $MaxActualDataFlatID = $db->getOne('SELECT MAX(l.ActualDataFlat_ID) FROM actual_data_flat_last l WHERE 1=1 ' .$asset_id);
        if(!is_numeric($AsyncData->data->MaxActualDataFlatID) or !strlen($AsyncData->data->MaxActualDataFlatID))
            $AsyncData->data->MaxActualDataFlatID = $MaxActualDataFlatID;
        //error_log($MaxActualDataFlatID->getDebugInfo());

        if(($AsyncData->data->MaxActualDataFlatID == $MaxActualDataFlatID))
            sleep(30);
        else
            sleep(15);

      // Nothing happen and die
        if($waittime<time())
            exit;
    } while($MaxActualDataFlatID==$AsyncData->data->MaxActualDataFlatID);
    $AsyncData->data->MaxActualDataFlatID = $MaxActualDataFlatID;

    if (strlen($data_id))
        $data_id = ' AND ((l.ID = ' . $data_id . ' AND l.Latitude<>0 AND l.Longitude<>0) OR (ID < ' . $data_id . ' AND Latitude<>0 AND Longitude<>0))';
    else
        $actual_data_last = true;

    if ($fleet_id == -1 or !strlen($fleet_id)) {
        $sql = 'SELECT m.id, m.Modul_ID, '.$sNameColumn.' FROM asset m WHERE 1=1 ' .$masset_id. ' AND m.id ' . rights::get_asset($db) . ' ORDER BY Name';
    }
    elseif ($fleet_id == 0) {
        $sql = 'SELECT m.id, m.Modul_ID, '.$sNameColumn.' FROM asset m
                    LEFT JOIN rel_fleet_asset r ON m.id=r.Asset_ID
                    WHERE 1=1 ' . $masset_id. ' ' . ' AND m.id ' . rights::get_asset($db) . ' ORDER BY Name';
    } else {
        $sql = 'SELECT m.id, m.Modul_ID, '.$sNameColumn.' FROM asset m
                      LEFT JOIN rel_fleet_asset r ON m.id=r.Asset_ID
                      WHERE  1=1 '.$masset_id. ' AND m.id ' . rights::get_asset($db) . '  ORDER BY Name';
    }

    $data = & $db->getAll($sql, DB_FETCHMODE_ASSOC);
    foreach ($data as $cur) {
        $sQueryWithUserDefinedColor = "";
        $sQueryWithUserDefinedColorField = "";
        $hasSensor = $db->getOne("SELECT ID FROM rel_modul_sensor WHERE ModulID=".$cur['Modul_ID']);
        if($hasSensor) {
            if(strlen($cur['Modul_ID'])) {
                $aRow = $db->getRow("SELECT p.FieldRelation, p.Condition, p.MapImage FROM rel_modul_sensor r LEFT JOIN sensor_profile p ON(r.SensorProfile_ID=p.ID) WHERE ModulID=".$cur['Modul_ID']);
                if (PEAR :: isError($aRow))
                    error_log($aRow->getDebugInfo());

                if(strlen($aRow['FieldRelation'])) {
                    $sQueryWithUserDefinedColor = 'LEFT JOIN actual_data_flat_field ff ON (l.ActualDataFlat_ID=ff.ActualDataFlat_ID AND ff.Name="'.$aRow['FieldRelation'].'" AND ff.description="'.$aRow['Condition'].'")';
                    $sQueryWithUserDefinedColorField = ', ff.ActualDataFlat_ID AS udc';
                }
            }
        }

        $sql = 'SELECT '.(($actual_data_last) ? 'l.ActualDataFlat_ID AS ID' : 'l.ID').', l.Latitude AS lat, l.Longitude AS lon, l.Status AS event, l.Speed AS speed, l.Heading AS dir'.$sQueryWithUserDefinedColorField.'
                FROM actual_data_flat_last l LEFT JOIN actual_data_flat_asset fa ON (l.ActualDataFlat_ID=fa.ActualDataFlat_ID)
                '.$sQueryWithUserDefinedColor.'
            WHERE fa.Asset_ID=' . $cur['id'] .' '. $asset_id . $data_id . ' ORDER BY l.ID DESC LIMIT 1';
        $data2 = & $db->getAll($sql, DB_FETCHMODE_ASSOC | DB_FETCHMODE_FLIPPED);
      if (PEAR :: isError($data2))
         error_log($data2->getDebugInfo());

        if($data2['lat'][0]==0 and $data2['lon'][0]==0)
            continue;
        else {
            $data2['lat'][0] = round($data2['lat'][0], 6);
            $data2['lon'][0] = round($data2['lon'][0], 6);
        }
        if(($data2['event'][0] & 4)>0)
            $data2['alert'][0] = true;
        unset($data2['event']);
