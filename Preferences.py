import bpy
from bpy.props import (
    BoolProperty,
    FloatProperty,
)
from bpy.types import AddonPreferences


def update_node_keymap(self, context):
    wm = context.window_manager
    active_kc = wm.keyconfigs.active
    for key in active_kc.keymaps["Node Editor"].keymap_items:
        if key.idname == "wm.call_menu" and key.type == "RIGHTMOUSE":
            key.active = not key.active

    addon_kc = wm.keyconfigs.addon
    for key in addon_kc.keymaps["Node Editor"].keymap_items:
        if key.idname == "rmn.right_mouse_navigation" and key.type == "RIGHTMOUSE":
            key.active = not key.active


def update_rebind_3dview_keymap(self, context):
    print(self.rmb_pan_rotate)
    self.rebind_3dview_keymap(context, self.rmb_pan_rotate)


def update_rebind_switch_nav_rotate(self, context):
    print(self.rmb_pan_rotate)
    self.rebind_switch_nav_rotate(context, self.rmb_rotate_switch)


class RightMouseNavigationPreferences(AddonPreferences):
    bl_idname = __package__

    time: FloatProperty(
        name="Time Threshold",
        description="How long you have hold right mouse to open menu",
        default=1.0,
        min=0.1,
        max=10,
    )

    reset_cursor_on_exit: BoolProperty(
        name="Reset Cursor on Exit",
        description="After exiting navigation, this determines if the cursor stays "
        "where RMB was clicked (if unchecked) or resets to the center (if checked)",
        default=False,
    )

    enable_for_node_editors: BoolProperty(
        name="Enable for Node Editors",
        description="Right Mouse will pan the view / open the Node Add/Search Menu",
        default=False,
        update=update_node_keymap,
    )

    rmb_pan_rotate: BoolProperty(
        name="Switch MMB and RMB Pan/Rotate",
        description="Switches Pan/Rotate (and more) controls to Right Mouse Button.",
        default=False,
        update=update_rebind_3dview_keymap,
    )

    rmb_rotate_switch: BoolProperty(
        name="Switch RMB Nav and Rotate Alt Modifier",
        description="Switches RMB Navigation and Pan/Rotate controls Alt modifier.",
        default=False,
        update=update_rebind_switch_nav_rotate,
    )

    def rebind_3dview_keymap(self, context, isActive):
        wm = context.window_manager
        active_kc = wm.keyconfigs.active
        addon_kc = wm.keyconfigs.addon
        
        if (isActive):
            # print("bind")
            for key in active_kc.keymaps["3D View"].keymap_items:
                if (key.idname == "view3d.cursor3d" and key.type == "RIGHTMOUSE"):
                    key.type = "MIDDLEMOUSE"
                    key.value = "CLICK"
                    key.shift = True
                if (key.idname == "view3d.rotate" and key.type == "MIDDLEMOUSE"):
                    key.type = "RIGHTMOUSE"
                    key.value = "CLICK_DRAG"
                    key.alt = True
                if (key.idname == "view3d.move" and key.type == "MIDDLEMOUSE"):
                    key.type = "RIGHTMOUSE"
                    key.value = "CLICK_DRAG"
                    key.shift = True
                if (key.idname == "view3d.zoom" and key.type == "MIDDLEMOUSE"):
                    key.type = "RIGHTMOUSE"
                    key.value = "CLICK_DRAG"
                    key.ctrl = True
                if (key.idname == "view3d.dolly" and key.type == "MIDDLEMOUSE"):
                    key.type = "RIGHTMOUSE"
                    key.value = "CLICK_DRAG"
                    key.shift = True
                    key.ctrl = True
                if (key.idname == "view3d.select_lasso" and key.type == "RIGHTMOUSE" and key.ctrl == True):
                    key.type = "MIDDLEMOUSE"
                    key.value = "CLICK_DRAG"
                    key.ctrl = True
                if (key.idname == "view3d.select_lasso" and key.type == "RIGHTMOUSE" and key.ctrl == True and key.shift == True):
                    key.type = "MIDDLEMOUSE"
                    key.value = "CLICK_DRAG"
                    key.shift = True
                    key.ctrl = True
                if (key.idname == "transform.translate" and key.type == "RIGHTMOUSE"):
                    key.type = "MIDDLEMOUSE"

        else:
            # print("unbind")
            for key in active_kc.keymaps["3D View"].keymap_items:
                if (key.idname == "view3d.cursor3d" and key.type == "MIDDLEMOUSE"):
                    key.type = "RIGHTMOUSE"
                    key.value = "CLICK"
                    key.shift = True
                if (key.idname == "view3d.rotate" and key.type == "RIGHTMOUSE"):
                    key.type = "MIDDLEMOUSE"
                    key.value = "PRESS"
                    key.alt = False
                if (key.idname == "view3d.move" and key.type == "RIGHTMOUSE"):
                    key.type = "MIDDLEMOUSE"
                    key.value = "PRESS"
                    key.shift = True
                if (key.idname == "view3d.zoom" and key.type == "RIGHTMOUSE"):
                    key.type = "MIDDLEMOUSE"
                    key.value = "PRESS"
                    key.ctrl = True
                if (key.idname == "view3d.dolly" and key.type == "RIGHTMOUSE"):
                    key.type = "MIDDLEMOUSE"
                    key.value = "PRESS"
                    key.shift = True
                    key.ctrl = True
                if (key.idname == "view3d.select_lasso" and key.type == "MIDDLEMOUSE" and key.ctrl == True):
                    key.type = "RIGHTMOUSE"
                    key.value = "CLICK_DRAG"
                    key.ctrl = True
                if (key.idname == "view3d.select_lasso" and key.type == "MIDDLEMOUSE" and key.ctrl == True and key.shift == True):
                    key.type = "RIGHTMOUSE"
                    key.value = "CLICK_DRAG"
                    key.shift = True
                    key.ctrl = True
                if (key.idname == "transform.translate" and key.type == "MIDDLEMOUSE"):
                    key.type = "RIGHTMOUSE"


    def rebind_switch_nav_rotate(self, context, isActive):
        wm = context.window_manager
        active_kc = wm.keyconfigs.active
        addon_kc = wm.keyconfigs.addon
        
        if (isActive):
            # print("bind")
            for key in addon_kc.keymaps["3D View"].keymap_items:
                if (key.idname == "rmn.right_mouse_navigation"):
                    key.type = "RIGHTMOUSE"
                    key.value = "PRESS"
                    key.alt = True
            for key in active_kc.keymaps["3D View"].keymap_items:
                if (key.idname == "view3d.rotate" and key.type == "RIGHTMOUSE"):
                    key.type = "RIGHTMOUSE"
                    key.value = "CLICK_DRAG"
                    key.alt = False

        else:
            # print("unbind")
            for key in addon_kc.keymaps["3D View"].keymap_items:
                if (key.idname == "rmn.right_mouse_navigation"):
                    key.type = "RIGHTMOUSE"
                    key.value = "PRESS"
                    key.alt = False
            for key in active_kc.keymaps["3D View"].keymap_items:
                if (key.idname == "view3d.rotate" and key.type == "RIGHTMOUSE"):
                    key.type = "RIGHTMOUSE"
                    key.value = "CLICK_DRAG"
                    key.alt = True


    def draw(self, context):
        layout = self.layout

        box = layout.box()
        box.label(text="Menu / Movement", icon="DRIVER_DISTANCE")
        box.prop(self, "time")

        row = layout.row()
        box = row.box()
        box.label(text="Cursor", icon="ORIENTATION_CURSOR")
        box.prop(self, "reset_cursor_on_exit")
        box = row.box()
        box.label(text="Node Editor", icon="NODETREE")
        box.prop(self, "enable_for_node_editors")
        
        row = layout.row()
        box = row.box()
        box.label(text="Right Mouse Button Pan/Rotate", icon="VIEW3D")
        box.prop(self, "rmb_pan_rotate")
        box.prop(self, "rmb_rotate_switch")
