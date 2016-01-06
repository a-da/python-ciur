WRONG
=====

.. code-block:: html

    <ul id="number" class="listing inlined" style='font-family: "Lucida Grande", Lucida, Verdana, sans-serif;margin: 4.0px 3.0px 2.0px 1.0px;padding: 0.0;background-color: yellow;'>
      <li class="list-element odd" style='font-family: "Lucida Grande", Lucida, Verdana, sans-serif;margin: 4.0px 3.0px 2.0px 1.0px;padding: 0.0;background-color: black;'>
        <span style='font-family: "Lucida Grande", Lucida, Verdana, sans-serif;margin: 4.0px 3.0px 2.0px 1.0px;padding: 0.0;'>1</span>
      </li>
      <li class="list-element pair" style='font-family: "Lucida Grande", Lucida, Verdana, sans-serif;margin: 4.0px 3.0px 2.0px 1.0px;padding: 0.0;background-color: red;'>
        <span style='font-family: "Lucida Grande", Lucida, Verdana, sans-serif;margin: 4.0px 3.0px 2.0px 1.0px;padding: 0.0;'>2</span>
      </li>
      <li class="list-element odd" style='font-family: "Lucida Grande", Lucida, Verdana, sans-serif;margin: 4.0px 3.0px 2.0px 1.0px;padding: 0.0;background-color: black;'>
        <span style='font-family: "Lucida Grande", Lucida, Verdana, sans-serif;margin: 4.0px 3.0px 2.0px 1.0px;padding: 0.0;'>3</span>
      </li>
      <li class="list-element pair" style='font-family: "Lucida Grande", Lucida, Verdana, sans-serif;margin: 4.0px 3.0px 2.0px 1.0px;padding: 0.0;background-color: red;'>
        <span style='font-family: "Lucida Grande", Lucida, Verdana, sans-serif;margin: 4.0px 3.0px 2.0px 1.0px;padding: 0.0;'>4</span>
      </li>
    </ul>

CORRECT
=======

.. code-block:: html

    <ul id='number' class='listing inlined' style='background-color: yellow'>
      <li class='list-element odd'>
        <span>1</span>
      </li>
      <li class='list-element pair'>
        <span>2</span>
      </li>
      <li class='list-element odd'>
        <span>3</span>
      </li>
      <li class='list-element pair'>
        <span>4</span>
      </li>
    </ul>
