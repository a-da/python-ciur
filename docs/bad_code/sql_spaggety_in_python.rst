.. code-block:: python

    if app_data is not None:
        delta_appcounter1 = app_data.app_counter1 - dragIndicator[LAST_APP_COUNT1]
        delta_appcounter2 = app_data.app_counter2 - dragIndicator[LAST_APP_COUNT2]

    query = """
                INSERT INTO `drag_indicator`
                    SET `ModulID`=%s,
                        `LastBattVoltage`=%s, `LastBattCap`=%s,
                        `LastBatteryCapmAs`=%s, `LastMileage`=%s,
                        `LastTimeStill`=%s, `LastTimeMoved`=%s,
                        `TotalBatteryCapmAs`=%s, `TotalMileage`=%s,
                        `TotalTimeStill`=%s, `TotalTimeMoved`=%s,
                        `LastAppCounter1`=%s, `LastAppCounter2`=%s,
                        `LastAppCounter3`=%s, `LastAppCounter4`=%s,
                        `TotalAppCounter1`=%s, `TotalAppCounter2`=%s,
                        `TotalAppCounter3`=%s, `TotalAppCounter4`=%s
                ON DUPLICATE KEY UPDATE
                    `LastBattVoltage`=VALUES(`LastBattVoltage`), `LastBattCap`=VALUES(`LastBattCap`),
                    `LastBatteryCapmAs`=VALUES(`LastBatteryCapmAs`), `LastMileage`=VALUES(`LastMileage`),
                    `LastTimeStill`=VALUES(`LastTimeStill`), `LastTimeMoved`=VALUES(`LastTimeMoved`),
                    `TotalBatteryCapmAs`=VALUES(`TotalBatteryCapmAs`), `TotalMileage`=VALUES(`TotalMileage`),
                    `TotalTimeStill`=VALUES(`TotalTimeStill`), `TotalTimeMoved`=VALUES(`TotalTimeMoved`),
                    `LastAppCounter1`=VALUES(`LastAppCounter1`), `LastAppCounter2`=VALUES(`LastAppCounter2`),
                    `LastAppCounter3`=VALUES(`LastAppCounter3`), `LastAppCounter4`=VALUES(`LastAppCounter4`),
                    `TotalAppCounter1`=VALUES(`TotalAppCounter1`), `TotalAppCounter2`=VALUES(`TotalAppCounter2`),
                    `TotalAppCounter3`=VALUES(`TotalAppCounter3`), `TotalAppCounter4`=VALUES(`TotalAppCounter4`)
            """ % (newDragIndicator[MODUL_ID], newDragIndicator[LAST_BAT_V], newDragIndicator[LAST_BAT_CAP],
                   newDragIndicator[LAST_BAT_CAP_MAS], newDragIndicator[LAST_MILEAGE], newDragIndicator[LAST_TIME_STILL],
                   newDragIndicator[LAST_TIME_MOVE], newDragIndicator[TOTAL_BAT_CAP_MAS], newDragIndicator[TOTAL_MILEAGE],
                   newDragIndicator[TOTAL_TIME_STILL], newDragIndicator[TOTAL_TIME_MOVE],
                   newDragIndicator[LAST_APP_COUNT1], newDragIndicator[LAST_APP_COUNT2],
                   newDragIndicator[LAST_APP_COUNT3], newDragIndicator[LAST_APP_COUNT4],
                   newDragIndicator[TOTAL_APP_COUNT1], newDragIndicator[TOTAL_APP_COUNT2],
                   newDragIndicator[TOTAL_APP_COUNT3], newDragIndicator[TOTAL_APP_COUNT4])
    cursor.execute(query)
    # -------------------------------------------------
    # Drag-Indicator End
    # -------------------------------------------------
    endTime = time.time()
    # TODO: be sure that we have at least one actual_data and actual_data_flat record
    # we need all information here, to get the ID
    stime = time.time()
    query = """
        INSERT INTO %s.`actual_data_flat`
            (`Modul_ID`,
            `TimestampUTC`,`PositionTimeUTC`,
            `Latitude`, `Longitude`, `Heading`, `Altitude`, `Satellites`,`Speed`,
            `EventTimeUTC`,`EventType`,`Status`,
            `IgnitionOn`, `VibrationOn`, `AlarmOn`, `PowerOn`, `Zone`, `ZoneName`,
            `Mileage`, `TimeStill`, `TimeMoved`, `InternCapacity`, `InternVoltage`, `ZoneType`,
            `AppCounter1`, `AppCounter2`, `AppCounter3`, `AppCounter4`)
            VALUES
            (%u,
            UTC_TIMESTAMP(), CONVERT_TZ(FROM_UNIXTIME('%s'), 'Europe/Zurich', 'UTC'),
            DEGREES(%u/POW(10, 8)), DEGREES(%u/POW(10, 8)), %u, %u, %u, %u,
            FROM_UNIXTIME('%s'), '%s', %u,
            %u & 1, (%u>>1) & 1, (%u>>2) & 1, (%u>>3) & 1, %u, "%s",
            %s.`FxMileageJustifyV4`(%u, UTC_TIMESTAMP())+%u, %u, %u, %s, %s, %s,
            %u, %u, %u, %u
            )""" % (
                self.central_db,
                modulId,
                pos_fix_time,
                pos_lat, pos_lon, pos_heading, pos_altitude, pos_num_sat, int(round(pos_speed * 0.36)),
                item[3], event_name, state & 63,
                state, state, state, state, zone_id, zone_name,
                self.central_db, modulId, newDragIndicator[TOTAL_MILEAGE], newDragIndicator[TOTAL_TIME_STILL],
                newDragIndicator[TOTAL_TIME_MOVE], int(round(batt_cap)), round(int(batt_voltage) / 1000.0, 1), zone_groups,
                newDragIndicator[TOTAL_APP_COUNT1], newDragIndicator[TOTAL_APP_COUNT2], newDragIndicator[TOTAL_APP_COUNT3],
                newDragIndicator[TOTAL_APP_COUNT4]
            )
    cursor.execute(query)

    query = "SELECT LAST_INSERT_ID()"
    cursor.execute(query)
    lastFlatId = cursor.fetchone()
    etime = time.time()
    totalTime = totalTime + (etime - stime) * 1000
    if priority == 3:
        """
        Store alert reference data
        """
        alarm_data_at.append("""("%s",UTC_TIMESTAMP(),"%s",FROM_UNIXTIME("%s"),0,"%s")""" %
                             (modulId, event_type, item[3], lastFlatId[0]))
    if (state & 64) > 0:
        actual_data_flat_direction.append("""(%u,%u,FROM_UNIXTIME("%s"),%u)""" %
                             (lastFlatId[0], modulId, item[3], (state >> 7) & 1))
