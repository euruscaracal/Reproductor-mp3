<?xml version="1.0" encoding="UTF-8"?>
<!-- Generated with glade 3.22.1 -->
<interface>
  <requires lib="gtk+" version="3.20"/>
  <object class="GtkWindow">
    <property name="can_focus">False</property>
    <child>
      <placeholder/>
    </child>
    <child>
      <object class="GtkBox">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <property name="orientation">vertical</property>
        <child>
          <object class="GtkSpinButton">
            <property name="visible">True</property>
            <property name="can_focus">True</property>
            <property name="shadow_type">etched-in</property>
            <property name="primary_icon_stock">gtk-justify-right</property>
            <property name="show_emoji_icon">True</property>
            <property name="update_policy">if-valid</property>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">0</property>
          </packing>
        </child>
        <child>
          <object class="GtkLabel">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="label" translatable="yes">track 01</property>
            <property name="use_underline">True</property>
            <property name="justify">right</property>
            <property name="selectable">True</property>
            <property name="ellipsize">end</property>
            <property name="xalign">0.5</property>
            <property name="yalign">0.5</property>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">1</property>
          </packing>
        </child>
        <child>
          <object class="GtkInfoBar">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <child internal-child="action_area">
              <object class="GtkButtonBox">
                <property name="can_focus">False</property>
                <property name="spacing">6</property>
                <property name="layout_style">end</property>
                <child>
                  <placeholder/>
                </child>
                <child>
                  <placeholder/>
                </child>
                <child>
                  <placeholder/>
                </child>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">False</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child internal-child="content_area">
              <object class="GtkBox">
                <property name="can_focus">False</property>
                <property name="spacing">16</property>
                <child>
                  <placeholder/>
                </child>
                <child>
                  <placeholder/>
                </child>
                <child>
                  <placeholder/>
                </child>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">False</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <placeholder/>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">2</property>
          </packing>
        </child>
        <child>
          <placeholder/>
        </child>
        <child>
          <placeholder/>
        </child>
      </object>
    </child>
  </object>
  <object class="GtkMenu">
    <property name="visible">True</property>
    <property name="can_focus">False</property>
  </object>
</interface>
