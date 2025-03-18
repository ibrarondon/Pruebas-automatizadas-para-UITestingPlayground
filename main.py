import time
from selenium.common import WebDriverException
import pyperclip
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.select import Select

import data
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
JS_DROP_FILES = "var k=arguments,d=k[0],g=k[1],c=k[2],m=d.ownerDocument||document;for(var e=0;;){var f=d.getBoundingClientRect(),b=f.left+(g||(f.width/2)),a=f.top+(c||(f.height/2)),h=m.elementFromPoint(b,a);if(h&&d.contains(h)){break}if(++e>1){var j=new Error('Element not interactable');j.code=15;throw j}d.scrollIntoView({behavior:'instant',block:'center',inline:'center'})}var l=m.createElement('INPUT');l.setAttribute('type','file');l.setAttribute('multiple','');l.setAttribute('style','position:fixed;z-index:2147483647;left:0;top:0;');l.onchange=function(q){l.parentElement.removeChild(l);q.stopPropagation();var r={constructor:DataTransfer,effectAllowed:'all',dropEffect:'none',types:['Files'],files:l.files,setData:function u(){},getData:function o(){},clearData:function s(){},setDragImage:function i(){}};if(window.DataTransferItemList){r.items=Object.setPrototypeOf(Array.prototype.map.call(l.files,function(x){return{constructor:DataTransferItem,kind:'file',type:x.type,getAsFile:function v(){return x},getAsString:function y(A){var z=new FileReader();z.onload=function(B){A(B.target.result)};z.readAsText(x)},webkitGetAsEntry:function w(){return{constructor:FileSystemFileEntry,name:x.name,fullPath:'/'+x.name,isFile:true,isDirectory:false,file:function z(A){A(x)}}}}}),{constructor:DataTransferItemList,add:function t(){},clear:function p(){},remove:function n(){}})}['dragenter','dragover','drop'].forEach(function(v){var w=m.createEvent('DragEvent');w.initMouseEvent(v,true,true,m.defaultView,0,0,0,b,a,false,false,false,false,0,null);Object.setPrototypeOf(w,null);w.dataTransfer=r;Object.setPrototypeOf(w,DragEvent.prototype);h.dispatchEvent(w)})};m.documentElement.appendChild(l);l.getBoundingClientRect();return l"


class UITestingPlayground:
    footer = (By. ID, "footer") #Footer locator to know when the web is loaded
    button_with_static_ID = (By.ID, "114a2baa-cc69-1ba1-e615-0de91881cee5")  # Button with dynamic ID
    button_with_dynamic_ID = (By.CLASS_NAME, "btn-primary") #Button with dynamic ID
    blue_button_by_class = (By.CLASS_NAME, "btn-primary") #Blue button
    hidden_layer_button = (By.CSS_SELECTOR, ".btn.btn-success") #hidden layer green button
    load_delay_button = (By.CLASS_NAME, "btn-primary")
    ajax_button = (By.CLASS_NAME, "btn-primary")
    ajax_label = (By.CSS_SELECTOR, ".bg-success")
    client_side_delay_button = (By.CLASS_NAME, "btn-primary")
    client_side_text_element = (By.CSS_SELECTOR, ".bg-success")
    click_button = (By.ID, "badButton")
    updating_button = (By.ID, "updatingButton")
    input_bar_updating_button = (By.ID, "newButtonName")
    scrollbars_button = (By.ID, "hidingButton") #Button hidden. Need to scroll to find it
    dynamic_table_data = (By.XPATH, "//div[@role='row']//*[contains(text(),'Chrome')]/parent::*/span[contains(text(),'%')]") #Locates the Chrome CPU usage in the table
    dynamic_data_reference = (By.CLASS_NAME, "bg-warning") #Locates the reference value
    text_element_with_spaces = (By.XPATH, "//span[@class='badge-secondary'][normalize-space(.)='Welcome UserName!']") #Finds the matching text in the Playground
    start_progress_bar_button = (By.ID, "startButton") #Locates the start button for progress bar
    stop_progress_bar_button = (By.ID, "stopButton") #Locates the stop button for progress bar
    progress_bar = (By.ID, "progressBar") #Locates the progress bar to get the progress
    progress_result = (By.ID, "result") #Locates the result of the progress
    visibility_hide_button = (By.ID, "hideButton") #Button to hide buttons on click
    visibility_removed_button = (By.CLASS_NAME, "btn-danger") #Removed button on visibility page
    visibility_zero_width_button  = (By.CLASS_NAME, "btn-warning") #Zero width button on visibility page
    visibility_overlapped_button = (By.CLASS_NAME, "btn-success") #Overlapped button on visibility page
    visibility_opacity_0_button = (By.XPATH, "//button[contains(text(),'Opacity')]") #Opacity 0 button on visibility page
    visibility_hidden_visibility_button = (By.XPATH, "//button[contains(text(),'Visibility Hidden')]") #Visibility 0 button on visibility page
    visibility_display_none_button = (By.XPATH, "//button[contains(text(),'Display None')]") #Display None button on visibility page
    visibility_offscreen_button = (By.XPATH, "//button[contains(text(),'Offscreen')]") #Offscreen button on visibility page
    username_field_sample_app = (By.NAME, "UserName") #Username field in sample app
    password_field_sample_app = (By.NAME, "Password") #Password field in sample app
    login_button_sample_app = (By.ID, "login") #Login button in sample app
    login_status_sample_app = (By.ID, "loginstatus") #Login result in sample app
    mouse_over_click_me =  (By.XPATH, "//a[contains(text(),'Click me')]") #Click me link in mouse over page
    mouse_over_click_me_count = (By.ID, "clickCount") #Click me count in mouse over page
    mouse_over_link_button = (By.XPATH, "//a[@title='Link Button']") #Link button in mouse over page
    mouse_over_link_button_count = (By.ID, "clickButtonCount") #Link button count in mouse over page
    non_breaking_space_button = (By.XPATH, "//button[@class='btn btn-primary'][contains(normalize-space(translate(/, '&#160;', ' ')), 'My Button')]")  # Finds the matching text with non-breaking space in the Playground
    overlapped_name_box = (By.ID, "name") #Name text box in overlapped element page
    guid_generator = (By.TAG_NAME, "guid-generator") #Guid Generator box in shadow DOM element page
    alerts_alert_button = (By.ID, "alertButton") #Alert button in alerts page
    alerts_confirm_button = (By.ID, "confirmButton") #Confirm button in alerts page
    alerts_prompt_button = (By.ID, "promptButton") #Prompt button in alerts page
    file_upload_input = (By.ID, 'browse') #Upload box with click in file upload page
    file_upload_status = (By.CLASS_NAME, "success-file") #Success message when uploading a file in file upload page
    animated_button_start_animation = (By.ID, "animationButton") #Start animation button in animated button page
    animated_button_moving_target = (By.ID, "movingTarget") #Animated moving button in animated button page
    animated_button_animation_status = (By.ID, "opstatus") #Animation status in animated button page
    disabled_input_enable_button = (By.ID, "enableButton") #Enable edit button in Disabled Input page
    disabled_input_input_status = (By.ID, "opstatus") #Status of the input in Disabled Input page
    disabled_input_input_field = (By.ID, "inputField") #Input field in Disabled Input page
    auto_wait_dropdown_list = (By.ID, "element-type") #Dropdown list with elements in Auto Wait page
    auto_wait_visible_checkbox = (By.ID, "visible") #Checkbox for visible attribute in Auto Wait page
    auto_wait_enabled_checkbox = (By.ID, "enabled") #Checkbox for enabled attribute in Auto Wait page
    auto_wait_editable_checkbox = (By.ID, "editable") #Checkbox for editable attribute in Auto Wait page
    auto_wait_ontop_checkbox = (By.ID, "ontop") #Checkbox for on top attribute in Auto Wait page
    auto_wait_nonzero_checkbox = (By.ID, "nonzero") #Checkbox for non zero attribute in Auto Wait page
    auto_wait_target_element = (By.ID, "target") #Target element for Auto Wait page tests
    auto_wait_select_item1 = (By.XPATH, "//select/option[contains(text(), 'Item 1')]")
    auto_wait_select_item2 = (By.XPATH, "//select/option[contains(text(), 'Item 2')]")
    auto_wait_select_item3 = (By.XPATH, "//select/option[contains(text(), 'Item 3')]")
    auto_wait_apply_3s_button = (By.ID, "applyButton3") #Apply 3s button in Auto Wait page
    auto_wait_apply_5s_button = (By.ID, "applyButton5") #Apply 5s button in Auto Wait page
    auto_wait_apply_10s_button = (By.ID, "applyButton10") #Apply 10s button in Auto Wait page
    auto_wait_operation_status = (By.ID, "opstatus") #Operation status in Auto Wait page


    def __init__(self, driver):
        self.driver = driver

    def find_static_ID_button(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.footer))
        return len(self.driver.find_elements(*self.button_with_static_ID))

    def find_dynamic_ID_button(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.footer))
        return len(self.driver.find_elements(*self.button_with_dynamic_ID))

    def click_blue_button_by_class(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.footer))
        self.driver.find_element(*self.blue_button_by_class).click() # Clicks the blue button

    def click_green_hidden_button(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.footer))
        self.driver.find_element(*self.hidden_layer_button).click()  # Clicks the green button
        try:
            self.driver.find_element(*self.hidden_layer_button).click()
            green_button_status = True
            return green_button_status
        except WebDriverException:
            green_button_status = False
            return green_button_status

    def wait_until_button_appears(self):
        WebDriverWait(self.driver, 8).until(expected_conditions.element_to_be_clickable(self.load_delay_button))
        return True

    def wait_until_ajax_response_shows_up(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.footer))
        self.driver.find_element(*self.ajax_button).click()
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(self.ajax_label))
        return self.driver.find_element(*self.ajax_label)

    def click_client_side_delay_button(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.footer))
        self.driver.find_element(*self.client_side_delay_button).click()

    def wait_for_client_element_to_show_up(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(self.client_side_text_element))
        return self.driver.find_element(*self.client_side_text_element)

    def get_button_color(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.footer))
        self.driver.find_element(*self.click_button).click()
        action = ActionChains(self.driver)
        action.move_by_offset(100,100).perform()
        WebDriverWait(self.driver, 2)
        background_color_rgba = self.driver.find_element(*self.click_button).value_of_css_property("background-color")
        background_color_hex =  Color.from_string(background_color_rgba).hex
        self.driver.find_element(*self.click_button).click()
        return background_color_hex

    def set_new_button_name(self,name):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.updating_button))
        self.driver.find_element(*self.input_bar_updating_button).send_keys(name)
        self.driver.find_element(*self.updating_button).click()

    def get_new_button_name(self):
        return self.driver.find_element(*self.updating_button)

    def scroll_to_button(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.footer))
        element = self.driver.find_element(*self.scrollbars_button)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform() #Can be scroll_to_element
        element.click()
        return element.is_displayed()

    def get_data_from_dynamic_table(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.footer))
        table_data = self.driver.find_element(*self.dynamic_table_data).text
        return table_data

    def get_reference_data_from_dynamic_table(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.footer))
        reference_data = self.driver.find_element(*self.dynamic_data_reference).text
        return reference_data

    def verify_text_with_spaces(self): #Test to find an element with text that contains spaces
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.footer))
        text = self.driver.find_element(*self.text_element_with_spaces).text
        return text

    def start_progress_bar(self): #Clicks the start button to start progress
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.start_progress_bar_button))
        self.driver.find_element(*self.start_progress_bar_button).click()

    def get_progress_bar(self): #Gets the % of the progress bar
        progress = int(self.driver.find_element(*self.progress_bar).get_attribute("aria-valuenow"))
        return progress

    def get_result_progress(self): #Gets the difference between the actual progress bar and the reference
        result = self.driver.find_element(*self.progress_result).text
        return result

    def stop_progress_bar(self): #Clicks the stop button to stop progress
        self.driver.find_element(*self.stop_progress_bar_button).click()

    def click_hide_visibility_button(self): #Clicks the hide button on visibility page
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.visibility_hide_button))
        self.driver.find_element(*self.visibility_hide_button)

    def get_visibility_of_removed_button(self): #Gets the visibility of Removed button on visibility page
        removed_button_visibility = self.driver.find_element(*self.visibility_removed_button).is_displayed()
        return removed_button_visibility

    def get_visibility_of_zero_width_button(self): #Gets the visibility of Zero width button on visibility page
        zero_width_button_visibility = self.driver.find_element(*self.visibility_zero_width_button).is_displayed()
        return zero_width_button_visibility

    def get_visibility_of_overlapped_button(self): #Gets the visibility of Overlapped button on visibility page
        overlapped_button_visibility = self.driver.find_element(*self.visibility_overlapped_button).is_displayed()
        return overlapped_button_visibility

    def get_visibility_of_opacity_0_button(self): #Gets the visibility of Opacity 0 button on visibility page
        opacity_0_button_visibility = self.driver.find_element(*self.visibility_opacity_0_button).is_displayed()
        return opacity_0_button_visibility

    def get_visibility_of_visibility_hidden_button(self): #Gets the visibility of Visibility hidden button on visibility page
        visibility_hidden_button_visibility = self.driver.find_element(*self.visibility_hidden_visibility_button).is_displayed()
        return visibility_hidden_button_visibility

    def get_visibility_of_display_none_button(self): #Gets the visibility of display none button on visibility page
        display_none_button_visibility = self.driver.find_element(*self.visibility_display_none_button).is_displayed()
        return display_none_button_visibility

    def get_visibility_of_offscreen_button(self): #Gets the visibility of Offscreen button on visibility page
        offscreen_button_visibility = self.driver.find_element(*self.visibility_offscreen_button).is_displayed()
        return offscreen_button_visibility

    def send_username(self,username): #Send username to login form
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.login_button_sample_app))
        self.driver.find_element(*self.username_field_sample_app).send_keys(username)

    def send_password(self,password): #Send password to login form
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.login_button_sample_app))
        self.driver.find_element(*self.password_field_sample_app).send_keys(password)

    def click_login_button(self): #Click login button to login
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.login_button_sample_app))
        self.driver.find_element(*self.login_button_sample_app).click()

    def get_login_status(self): #Get login status
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.login_button_sample_app))
        login_status = self.driver.find_element(*self.login_status_sample_app).text
        return login_status

    def click_click_me_link(self): #Clicks click me link
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.mouse_over_click_me))
        self.driver.find_element(*self.mouse_over_click_me).click()

    def get_click_me_count(self): #Gets the count of clicks on click me link
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.mouse_over_click_me_count))
        click_me_count = self.driver.find_element(*self.mouse_over_click_me_count).text
        return click_me_count

    def click_link_button(self):  # Clicks link button
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.mouse_over_link_button))
        self.driver.find_element(*self.mouse_over_link_button).click()

    def get_link_button_count(self):  # Gets the count of clicks on link button
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.mouse_over_link_button_count))
        click_me_count = self.driver.find_element(*self.mouse_over_link_button_count).text
        return click_me_count

    def click_non_breaking_space_button(self): #Clicks My Button in non-breaking space page
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.non_breaking_space_button))
        self.driver.find_element(*self.non_breaking_space_button).click()
        return True

    def set_name_overlapped_element(self): #Set an ID in the overlapped element page
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.overlapped_name_box))
        name_box = self.driver.find_element(*self.overlapped_name_box)
        self.driver.execute_script("arguments[0].scrollIntoView();",name_box) #scrolls until box is in viewport
        name_box.send_keys("Name")
        return name_box.is_displayed()

    def generate_guid(self): #Interact with Shadow DOM to generate a GUID, copy to clipboard and get text from input
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.guid_generator))
        shadow = self.driver.find_element(*self.guid_generator).shadow_root #Obtains shadow object
        shadow.find_element(By.CSS_SELECTOR, "button.button-generate").click()
        shadow.find_element(By.CSS_SELECTOR, "button.button-copy").click()
        copied_guid = pyperclip.paste()
        guid_generated = shadow.find_element(By.CSS_SELECTOR, "input.edit-field").text #Copies the generated guid in the input box
        return copied_guid, guid_generated

    def click_alert_button(self): #Click alert button in alerts page
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.alerts_alert_button))
        self.driver.find_element(*self.alerts_alert_button).click()
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert_text = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()  # Click accept in the JS alert
        return alert_text

    def click_confirm_button(self): #Click confirm button in alerts page
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.alerts_confirm_button))
        self.driver.find_element(*self.alerts_confirm_button).click()
        WebDriverWait(self.driver, 5).until(alert_is_present())
        confirm_alert_text = self.driver.switch_to.alert.text
        return confirm_alert_text

    def click_accept_confirm_button(self): #Click OK in confirm alert after clicking the confirm button
        self.driver.switch_to.alert.accept()
        WebDriverWait(self.driver, 5).until(alert_is_present())
        accepted_alert_text = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        return accepted_alert_text

    def click_cancel_confirm_button(self): #Click cancel in confirm alert after clicking the confirm button
        self.driver.switch_to.alert.dismiss()
        WebDriverWait(self.driver, 5).until(alert_is_present())
        cancelled_alert_text = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        return cancelled_alert_text

    def click_prompt_button_confirm(self,value): #Click prompt button in alerts page and confirm the action with non-default value
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.alerts_prompt_button))
        self.driver.find_element(*self.alerts_prompt_button).click()
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert
        alert.send_keys(value)
        alert.accept()
        WebDriverWait(self.driver, 5).until(alert_is_present())
        new_alert_text = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        return new_alert_text

    def click_prompt_button_cancel(self): #Click prompt button in alerts page and cancel the action
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.alerts_prompt_button))
        self.driver.find_element(*self.alerts_prompt_button).click()
        WebDriverWait(self.driver, 5).until(alert_is_present())
        alert = self.driver.switch_to.alert
        alert.dismiss()
        WebDriverWait(self.driver, 5).until(alert_is_present())
        new_alert_text = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        return new_alert_text

    def upload_document_with_browse_button(self): #Upload documents using 'Browse files' button
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.footer))
        self.driver.switch_to.frame(0) #Switch to the iframe that contains the button
        upload = self.driver.find_element(*self.file_upload_input)
        upload.send_keys("C:/Users/ibrac/OneDrive/Documentos/PyCharm/UItestingPlayground/example_file.txt")
        success_msg = self.driver.find_element(*self.file_upload_status).text
        return success_msg

    def click_start_animation_button(self): #Clicks start animation button in animated button page
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.animated_button_start_animation))
        self.driver.find_element(*self.animated_button_start_animation).click()
        animation_status = self.driver.find_element(*self.animated_button_animation_status).text
        return animation_status

    def click_moving_target_button(self): #Clicks moving target button after animation ends in animated button page
        animation_status = self.driver.find_element(*self.animated_button_animation_status).text
        while (animation_status == 'Animating the button...'):
            animation_status = self.driver.find_element(*self.animated_button_animation_status).text
        self.driver.find_element(*self.animated_button_moving_target).click()
        animation_status = self.driver.find_element(*self.animated_button_animation_status).text
        return animation_status

    def click_disable_button(self): #Click the button to disable the input
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.disabled_input_enable_button))
        self.driver.find_element(*self.disabled_input_enable_button).click()
        input_status = self.driver.find_element(*self.disabled_input_input_status).text
        return input_status

    def wait_until_input_enabled(self): #Waits until input field is enabled
        input_status = self.driver.find_element(*self.disabled_input_input_status).text
        while input_status == "Input Disabled...":
            input_status = self.driver.find_element(*self.disabled_input_input_status).text
        return input_status

    def enter_text_into_input_field(self, text): #Enters text into input field when enabled
        input_status = self.wait_until_input_enabled()
        assert input_status == "Input Enabled..."
        self.driver.find_element(*self.disabled_input_input_field).send_keys(text)
        self.driver.find_element(*self.disabled_input_input_status).click()
        return self.driver.find_element(*self.disabled_input_input_status).text

    def select_button_element_from_settings(self): #Select button from the dropdown list
        dropdown = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.auto_wait_dropdown_list))
        select = Select(dropdown)
        select.select_by_value("button")
        selected_option = select.first_selected_option
        assert selected_option.text == "Button"

    def select_input_element_from_settings(self): #Select button from the dropdown list
        dropdown = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.auto_wait_dropdown_list))
        select = Select(dropdown)
        select.select_by_value("input")
        selected_option = select.first_selected_option
        assert selected_option.text == "Input"

    def select_textarea_element_from_settings(self): #Select button from the dropdown list
        dropdown = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.auto_wait_dropdown_list))
        select = Select(dropdown)
        select.select_by_value("textarea")
        selected_option = select.first_selected_option
        assert selected_option.text == "Textarea"

    def select_select_element_from_settings(self): #Select button from the dropdown list
        dropdown = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.auto_wait_dropdown_list))
        select = Select(dropdown)
        select.select_by_value("select")
        selected_option = select.first_selected_option
        assert selected_option.text == "Select"

    def select_target_dropdown(self,item): #Select button from the dropdown list using send_keys
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.auto_wait_target_element))
        if item == 1:
            self.driver.find_element(*self.auto_wait_target_element).send_keys("Item 1")
        elif item == 2:
            self.driver.find_element(*self.auto_wait_target_element).send_keys("Item 2")
        elif item == 3:
            self.driver.find_element(*self.auto_wait_target_element).send_keys("Item 3")
        opstatus = self.driver.find_element(*self.auto_wait_operation_status).text
        return opstatus

    def select_label_element_from_settings(self): #Select button from the dropdown list
        dropdown = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.auto_wait_dropdown_list))
        select = Select(dropdown)
        select.select_by_value("label")
        selected_option = select.first_selected_option
        assert selected_option.text == "Label"

    def status_visible_checkbox(self): #Clicks the Visible checkbox
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.auto_wait_visible_checkbox))
        return self.driver.find_element(*self.auto_wait_visible_checkbox).is_selected()

    def click_visible_checkbox(self): #Clicks the Visible checkbox
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.auto_wait_visible_checkbox))
        assert self.status_visible_checkbox() == True
        self.driver.find_element(*self.auto_wait_visible_checkbox).click()
        return self.driver.find_element(*self.auto_wait_visible_checkbox).is_selected()

    def status_enabled_checkbox(self): #Clicks the Enabled checkbox
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.auto_wait_enabled_checkbox))
        return self.driver.find_element(*self.auto_wait_enabled_checkbox).is_selected()

    def click_enabled_checkbox(self): #Clicks the Enabled checkbox
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.auto_wait_enabled_checkbox))
        assert self.status_enabled_checkbox() == True
        self.driver.find_element(*self.auto_wait_enabled_checkbox).click()
        return self.driver.find_element(*self.auto_wait_enabled_checkbox).is_selected()

    def status_editable_checkbox(self):  # Clicks the Editable checkbox
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.auto_wait_editable_checkbox))
        return self.driver.find_element(*self.auto_wait_editable_checkbox).is_selected()

    def click_editable_checkbox(self):  # Clicks the Editable checkbox
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.auto_wait_editable_checkbox))
        assert self.status_editable_checkbox() == True
        self.driver.find_element(*self.auto_wait_editable_checkbox).click()
        return self.driver.find_element(*self.auto_wait_editable_checkbox).is_selected()

    def status_ontop_checkbox(self): #Clicks the On Top checkbox
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.auto_wait_ontop_checkbox))
        return self.driver.find_element(*self.auto_wait_ontop_checkbox).is_selected()

    def click_ontop_checkbox(self): #Clicks the On Top checkbox
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.auto_wait_ontop_checkbox))
        assert self.status_ontop_checkbox() == True
        self.driver.find_element(*self.auto_wait_ontop_checkbox).click()
        return self.driver.find_element(*self.auto_wait_ontop_checkbox).is_selected()

    def status_nonzero_checkbox(self): #Clicks the Non Zero Size checkbox
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.auto_wait_nonzero_checkbox))
        return self.driver.find_element(*self.auto_wait_nonzero_checkbox).is_selected()

    def click_nonzero_checkbox(self): #Clicks the Non Zero Size checkbox
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.auto_wait_nonzero_checkbox))
        assert self.status_nonzero_checkbox() == True
        self.driver.find_element(*self.auto_wait_nonzero_checkbox).click()
        return self.driver.find_element(*self.auto_wait_nonzero_checkbox).is_selected()

    def click_apply_3s_button(self): #Clicks the Apply 3s button
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.auto_wait_apply_3s_button))
        self.driver.find_element(*self.auto_wait_apply_3s_button).click()
        opstatus = self.driver.find_element(*self.auto_wait_operation_status).text
        time.sleep(3)
        return opstatus

    def click_apply_5s_button(self): #Clicks the Apply 3s button
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.auto_wait_apply_5s_button))
        self.driver.find_element(*self.auto_wait_apply_5s_button).click()
        opstatus = self.driver.find_element(*self.auto_wait_operation_status).text
        time.sleep(5)
        return opstatus

    def click_apply_10s_button(self): #Clicks the Apply 3s button
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.auto_wait_apply_10s_button))
        self.driver.find_element(*self.auto_wait_apply_10s_button).click()
        opstatus = self.driver.find_element(*self.auto_wait_operation_status).text
        time.sleep(10)
        return opstatus

    def click_auto_wait_target(self): #Clicks the target element
        self.driver.find_element(*self.auto_wait_target_element).click()
        opstatus = self.driver.find_element(*self.auto_wait_operation_status).text
        return opstatus

    def type_text_in_target(self,text): #Type text into target field
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.auto_wait_target_element))
        self.driver.find_element(*self.auto_wait_target_element).send_keys(text)
        self.driver.find_element(*self.auto_wait_dropdown_list).click()
        opstatus = self.driver.find_element(*self.auto_wait_operation_status).text
        return opstatus

    def select_item1_in_playground(self): #Select item 1 from dropdown list in playground
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.auto_wait_target_element))
        self.driver.find_element(*self.auto_wait_target_element).select_by_value("Item 1")
        assert self.driver.find_element(*self.auto_wait_target_element).first_selected_option == "Item 1"
        opstatus = self.driver.find_element(*self.auto_wait_operation_status).text
        assert opstatus == "Selected: Item 1"

    def select_item2_in_playground(self): #Select item 2 from dropdown list in playground
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.auto_wait_target_element))
        self.driver.find_element(*self.auto_wait_target_element).select_by_value("Item 2")
        assert self.driver.find_element(*self.auto_wait_target_element).first_selected_option == "Item 2"
        opstatus = self.driver.find_element(*self.auto_wait_operation_status).text
        assert opstatus == "Selected: Item 2"

    def select_item3_in_playground(self): #Select item 3 from dropdown list in playground
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.auto_wait_target_element))
        self.driver.find_element(*self.auto_wait_target_element).select_by_value("Item 3")
        assert self.driver.find_element(*self.auto_wait_target_element).first_selected_option == "Item 3"
        opstatus = self.driver.find_element(*self.auto_wait_operation_status).text
        assert opstatus == "Selected: Item 3"

    def enter_text_into_target_field(self,text): #Enters text in target field
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.auto_wait_target_element))
        self.driver.find_element(*self.auto_wait_target_element).send_keys(text)
        self.driver.find_element(*self.auto_wait_target_element).send_keys(Keys.TAB)
        opstatus = self.driver.find_element(*self.auto_wait_operation_status).text
        return opstatus

    def clear_text_in_target_field(self):
        self.driver.find_element(*self.auto_wait_target_element).clear()

class TestUIPlayground:

    driver = None

    @classmethod
    def setup_class(cls): #Starts Chrome Browser
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_dynamic_id_button(self): #Test to find a button with dynamic ID
        self.driver.get(data.automation_playground_url+data.dynamic_id_url)
        playground_page = UITestingPlayground(self.driver)
        buttons_by_ID = playground_page.find_static_ID_button()
        assert buttons_by_ID == 0, "Buttons were found by dynamic ID"
        buttons_by_class = playground_page.find_dynamic_ID_button()
        assert buttons_by_class == 1, "No buttons were found with class locator"

    def test_button_with_alert(self): #Test to find a specific button by class
        self.driver.get(data.automation_playground_url + data.class_attribute_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.click_blue_button_by_class()
        text = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept() #Click accept in the JS alert
        assert text == "Primary button pressed"

    def test_hidden_layers(self): #Test to click an inactive button
        self.driver.get(data.automation_playground_url + data.hidden_layers_url)
        playground_page = UITestingPlayground(self.driver)
        green_button_status = playground_page.click_green_hidden_button()
        assert green_button_status == False , "Inactive button is clickable"

    def test_load_delay(self): #Test to wait until the page loads
        self.driver.get(data.automation_playground_url + data.load_delay_url)
        playground_page = UITestingPlayground(self.driver)
        displayed = playground_page.wait_until_button_appears()
        assert displayed == True , "Page never loaded"

    def test_wait_ajax_data(self): #Test to wait until an element shows up
        self.driver.get(data.automation_playground_url + data.ajax_data_url)
        playground_page = UITestingPlayground(self.driver)
        ajax_data = playground_page.wait_until_ajax_response_shows_up().text
        assert ajax_data == "Data loaded with AJAX get request."

    def test_client_delay(self): #Test to wait until client element shows up
        self.driver.get(data.automation_playground_url + data.client_side_delay)
        playground_page = UITestingPlayground(self.driver)
        playground_page.click_client_side_delay_button()
        element_text = playground_page.wait_for_client_element_to_show_up().text
        assert element_text == "Data calculated on the client side."

    def test_click(self): #Test to confirm a button changes the color after being clicked
        self.driver.get(data.automation_playground_url + data.click_url)
        playground_page = UITestingPlayground(self.driver)
        background_color = playground_page.get_button_color()
        assert background_color == "#28a745" #HEX color taken from devtools

    def test_change_button_text(self, name = "NewButtonName"): #Test to change a button name with an input
        self.driver.get(data.automation_playground_url + data.text_input_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.set_new_button_name(name)
        new_button_name = playground_page.get_new_button_name().text
        assert new_button_name == name

    def test_scrollbars(self): #Test to scroll, click a button and confirm it is displayed
        self.driver.get(data.automation_playground_url + data.scrollbars_url)
        playground_page = UITestingPlayground(self.driver)
        button_displayed = playground_page.scroll_to_button()
        assert button_displayed == True , "Button was not displayed"

    def test_dynamic_table_data(self): #Test to get data from a dynamic table and compare it to a reference
        self.driver.get(data.automation_playground_url + data.dynamic_table_url)
        playground_page = UITestingPlayground(self.driver)
        dynamic_data = playground_page.get_data_from_dynamic_table()
        reference_data = playground_page.get_reference_data_from_dynamic_table()
        assert dynamic_data in reference_data, "The data does not match"

    def test_verify_text(self): #Test to verify an element with text was found properly
        self.driver.get(data.automation_playground_url + data.verify_text_url)
        playground_page = UITestingPlayground(self.driver)
        text = playground_page.verify_text_with_spaces()
        assert text == "Welcome UserName!"

    def test_progress_bar(self): #Test to stop a progress when the result is 75%
        self.driver.get(data.automation_playground_url + data.progress_bar_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.start_progress_bar()
        progress = 0
        while progress < 75: #Confirms progress is 75%
            progress = playground_page.get_progress_bar()
        else:
            playground_page.stop_progress_bar()
        result = playground_page.get_result_progress()
        assert "Result: 0" in result

    def test_visibility_page(self): #Test to get the visibility of buttons
        self.driver.get(data.automation_playground_url + data.visibility_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.click_hide_visibility_button()
        removed_button_visibility = playground_page.get_visibility_of_removed_button()
        zero_width_button_visibility = playground_page.get_visibility_of_zero_width_button()
        overlapped_button_visibility = playground_page.get_visibility_of_overlapped_button()
        opacity_0_button_visibility = playground_page.get_visibility_of_opacity_0_button()
        visibility_hidden_button_visibility = playground_page.get_visibility_of_visibility_hidden_button()
        display_none_button_visibility = playground_page.get_visibility_of_display_none_button()
        offscreen_button_visibility = playground_page.get_visibility_of_offscreen_button()
        assert removed_button_visibility is True
        assert zero_width_button_visibility is True
        assert overlapped_button_visibility is True
        assert opacity_0_button_visibility is True
        assert visibility_hidden_button_visibility is True
        assert display_none_button_visibility is True
        assert offscreen_button_visibility is True

    def test_positive_login_sample_app(self,username = "user",password = "pwd"): #Test to log in with valid username and password
        self.driver.get(data.automation_playground_url + data.sample_app_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.send_username(username)
        playground_page.send_password(password)
        playground_page.click_login_button()
        login_status = playground_page.get_login_status()
        welcome_msg = f'Welcome, {username}!'
        assert login_status == welcome_msg

    def test_empty_password_sample_app(self,username = "user",password = ""): #Test to log in with empty password
        self.driver.get(data.automation_playground_url + data.sample_app_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.send_username(username)
        playground_page.send_password(password)
        playground_page.click_login_button()
        login_status = playground_page.get_login_status()
        assert login_status == "Invalid username/password"

    def test_empty_username_and_password_sample_app(self,username = "",password = ""): #Test to log in with empty username and password
        self.driver.get(data.automation_playground_url + data.sample_app_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.send_username(username)
        playground_page.send_password(password)
        playground_page.click_login_button()
        login_status = playground_page.get_login_status()
        assert login_status == "Invalid username/password"

    def test_invalid_password_sample_app(self,username = "user",password = "password"): #Test to log in with invalid password
        self.driver.get(data.automation_playground_url + data.sample_app_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.send_username(username)
        playground_page.send_password(password)
        playground_page.click_login_button()
        login_status = playground_page.get_login_status()
        assert login_status == "Invalid username/password"

    def test_numeric_password_sample_app(self,username = "user",password = "123"): #Test to log in with numeric password
        self.driver.get(data.automation_playground_url + data.sample_app_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.send_username(username)
        playground_page.send_password(password)
        playground_page.click_login_button()
        login_status = playground_page.get_login_status()
        assert login_status == "Invalid username/password"

    def test_1space_password_sample_app(self,username = "user",password = " "): #Test to log in with one space password
        self.driver.get(data.automation_playground_url + data.sample_app_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.send_username(username)
        playground_page.send_password(password)
        playground_page.click_login_button()
        login_status = playground_page.get_login_status()
        assert login_status == "Invalid username/password"

    def test_1special_char_password_sample_app(self,username = "user",password = "-"): #Test to log in with one special character password
        self.driver.get(data.automation_playground_url + data.sample_app_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.send_username(username)
        playground_page.send_password(password)
        playground_page.click_login_button()
        login_status = playground_page.get_login_status()
        assert login_status == "Invalid username/password"

    def test_password_with_special_char_sample_app(self,username = "user",password = "pwd-"): #Test to log in with special character password
        self.driver.get(data.automation_playground_url + data.sample_app_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.send_username(username)
        playground_page.send_password(password)
        playground_page.click_login_button()
        login_status = playground_page.get_login_status()
        assert login_status == "Invalid username/password"

    def test_empty_username_sample_app(self,username = "",password = "pwd"): #Test to log in with empty username
        self.driver.get(data.automation_playground_url + data.sample_app_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.send_username(username)
        playground_page.send_password(password)
        playground_page.click_login_button()
        login_status = playground_page.get_login_status()
        assert login_status == "Invalid username/password"

    def test_1char_username_sample_app(self,username = "u",password = "pwd"): #Test to log in with 1 char username
        self.driver.get(data.automation_playground_url + data.sample_app_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.send_username(username)
        playground_page.send_password(password)
        playground_page.click_login_button()
        login_status = playground_page.get_login_status()
        welcome_msg = "Welcome, " + username + "!"
        assert login_status == welcome_msg

    def test_1space_username_sample_app(self,username = " ",password = "pwd"): #Test to log in with 1 space username
        self.driver.get(data.automation_playground_url + data.sample_app_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.send_username(username)
        playground_page.send_password(password)
        playground_page.click_login_button()
        login_status = playground_page.get_login_status()
        welcome_msg = f'Welcome, {username}!'
        assert login_status == welcome_msg

    def test_1special_char_username_sample_app(self,username = "-",password = "pwd"): #Test to log in with one special character username
        self.driver.get(data.automation_playground_url + data.sample_app_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.send_username(username)
        playground_page.send_password(password)
        playground_page.click_login_button()
        login_status = playground_page.get_login_status()
        welcome_msg = f'Welcome, {username}!'
        assert login_status == welcome_msg

    def test_username_with_space_sample_app(self,username = "us er",password = "pwd"): #Test to log in with username with one space
        self.driver.get(data.automation_playground_url + data.sample_app_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.send_username(username)
        playground_page.send_password(password)
        playground_page.click_login_button()
        login_status = playground_page.get_login_status()
        welcome_msg = f'Welcome, {username}!'
        assert login_status == welcome_msg

    def test_username_with_special_character_sample_app(self,username = "us-er",password = "pwd"): #Test to log in with username with one special character
        self.driver.get(data.automation_playground_url + data.sample_app_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.send_username(username)
        playground_page.send_password(password)
        playground_page.click_login_button()
        login_status = playground_page.get_login_status()
        welcome_msg = f'Welcome, {username}!'
        assert login_status == welcome_msg

    def test_mouse_over(self): #Tests mouse over changing elements
        self.driver.get(data.automation_playground_url + data.mouse_over_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.click_click_me_link()
        playground_page.click_click_me_link() #click the link twice
        click_me_count = playground_page.get_click_me_count()
        playground_page.click_link_button()
        playground_page.click_link_button() #click the link twice
        link_button_count = playground_page.get_link_button_count()
        assert click_me_count == "2"
        assert link_button_count == "2"

    def test_non_breaking_space(self): #Test to find a button with non-breaking space
        self.driver.get(data.automation_playground_url + data.non_breaking_space_url)
        playground_page = UITestingPlayground(self.driver)
        result = playground_page.click_non_breaking_space_button()
        assert result == True

    def test_overlapped_element(self): #Test to enter text to a partially visible element
        self.driver.get(data.automation_playground_url + data.overlapped_element_url)
        playground_page = UITestingPlayground(self.driver)
        element_is_displayed = playground_page.set_name_overlapped_element()
        assert element_is_displayed == True

    def test_shadow_dom(self): #Test to interact with shadow DOM elements and copy to clipboard
        self.driver.get(data.automation_playground_url + data.shadow_dom_url)
        playground_page = UITestingPlayground(self.driver)
        copied_guid, guid_generated = playground_page.generate_guid()
        assert copied_guid == guid_generated

    def test_alert_button(self): #Test to manage alert button alert in alerts page
        self.driver.get(data.automation_playground_url + data.alerts_url)
        playground_page = UITestingPlayground(self.driver)
        alert_text = playground_page.click_alert_button()
        assert "Today is a working day." in alert_text

    def test_accept_confirm_button(self):  # Test to manage confirm button alerts and accept it in alerts page
        self.driver.get(data.automation_playground_url + data.alerts_url)
        playground_page = UITestingPlayground(self.driver)
        confirm_alert_text = playground_page.click_confirm_button()
        assert "Today is Friday" in confirm_alert_text
        accept_confirm_text = playground_page.click_accept_confirm_button()
        assert accept_confirm_text == "Yes"

    def test_cancel_confirm_button(self):  # Test to manage confirm button alerts and cancel it in alerts page
        self.driver.get(data.automation_playground_url + data.alerts_url)
        playground_page = UITestingPlayground(self.driver)
        confirm_alert_text = playground_page.click_confirm_button()
        assert "Today is Friday" in confirm_alert_text
        cancel_confirm_text = playground_page.click_cancel_confirm_button()
        assert cancel_confirm_text == "No"

    def test_accept_prompt_button(self, value="dogs"): #Test to send keys to a prompt and accept in alerts page
        self.driver.get(data.automation_playground_url + data.alerts_url)
        playground_page = UITestingPlayground(self.driver)
        alert_text = playground_page.click_prompt_button_confirm(value)
        assert alert_text == f"User value: {value}"

    def test_cancel_prompt_button(self): #Test to cancel the process to send keys to a prompt in alerts page
        self.driver.get(data.automation_playground_url + data.alerts_url)
        playground_page = UITestingPlayground(self.driver)
        alert_text = playground_page.click_prompt_button_cancel()
        assert alert_text == f"User value: no answer"

    def test_upload_file(self): #Test to upload a document with clicks and file location in upload file page
        self.driver.get(data.automation_playground_url + data.upload_url)
        playground_page = UITestingPlayground(self.driver)
        upload_status = playground_page.upload_document_with_browse_button()
        assert "file(s) selected" in upload_status

    def test_animated_button(self): #Test to click a button after it's animated
        self.driver.get(data.automation_playground_url + data.animation_url)
        playground_page = UITestingPlayground(self.driver)
        animation_status = playground_page.click_start_animation_button()
        assert animation_status == 'Animating the button...'
        animation_status = playground_page.click_moving_target_button()
        assert animation_status == "Moving Target clicked. It's class name is 'btn btn-primary'"

    def test_disabled_input(self, text = "Test"): #Test to enter text as soon as an input field becomes enabled
        self.driver.get(data.automation_playground_url + data.disabled_input_url)
        playground_page = UITestingPlayground(self.driver)
        input_field_status = playground_page.click_disable_button()
        assert input_field_status == "Input Disabled..."
        input_text = playground_page.enter_text_into_input_field(text)
        assert input_text == f"Value changed to: {text}"

    def test_click_full_button(self, apply_time = 3): #Test to click button with all the properties checked in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_button_element_from_settings()
        assert playground_page.status_visible_checkbox() == True
        assert playground_page.status_enabled_checkbox() == True
        assert playground_page.status_editable_checkbox() == True
        assert playground_page.status_ontop_checkbox() == True
        assert playground_page.status_nonzero_checkbox() == True
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.click_auto_wait_target()
        assert target_msg == "Target clicked."

    def test_click_only_visible_button(self, apply_time=5):  # Test to click button with only visible checked in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_button_element_from_settings()
        assert playground_page.status_visible_checkbox() == True
        playground_page.click_enabled_checkbox()
        assert playground_page.status_enabled_checkbox() == False
        playground_page.click_editable_checkbox()
        assert playground_page.status_editable_checkbox() == False
        playground_page.click_ontop_checkbox()
        assert playground_page.status_ontop_checkbox() == False
        playground_page.click_nonzero_checkbox()
        assert playground_page.status_nonzero_checkbox() == False
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.click_auto_wait_target()
        assert target_msg == "Target clicked."

    def test_click_editable_nonzero_button(self, apply_time=5):  # Test to click button with editable and nonzero checked in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_button_element_from_settings()
        playground_page.click_visible_checkbox()
        assert playground_page.status_visible_checkbox() == False
        playground_page.click_enabled_checkbox()
        assert playground_page.status_enabled_checkbox() == False
        assert playground_page.status_editable_checkbox() == True
        playground_page.click_ontop_checkbox()
        assert playground_page.status_ontop_checkbox() == False
        assert playground_page.status_nonzero_checkbox() == True
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.click_auto_wait_target()
        assert target_msg == "Target clicked."

    def test_click_enabled_ontop_button(self, apply_time=10):  # Test to click button with editable and on top checked in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_button_element_from_settings()
        playground_page.click_visible_checkbox()
        assert playground_page.status_visible_checkbox() == False
        assert playground_page.status_enabled_checkbox() == True
        playground_page.click_editable_checkbox()
        assert playground_page.status_editable_checkbox() == False
        assert playground_page.status_ontop_checkbox() == True
        playground_page.click_nonzero_checkbox()
        assert playground_page.status_nonzero_checkbox() == False
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.click_auto_wait_target()
        assert target_msg == "Target clicked."

    def test_click_full_input(self, apply_time = 3): #Test to click input with all the properties checked in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_input_element_from_settings()
        assert playground_page.status_visible_checkbox() == True
        assert playground_page.status_enabled_checkbox() == True
        assert playground_page.status_editable_checkbox() == True
        assert playground_page.status_ontop_checkbox() == True
        assert playground_page.status_nonzero_checkbox() == True
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.click_auto_wait_target()
        assert target_msg == "Target clicked."

    def test_click_only_visible_input(self, apply_time=5):  # Test to click button with only visible checked in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_button_element_from_settings()
        assert playground_page.status_visible_checkbox() == True
        playground_page.click_enabled_checkbox()
        assert playground_page.status_enabled_checkbox() == False
        playground_page.click_editable_checkbox()
        assert playground_page.status_editable_checkbox() == False
        playground_page.click_ontop_checkbox()
        assert playground_page.status_ontop_checkbox() == False
        playground_page.click_nonzero_checkbox()
        assert playground_page.status_nonzero_checkbox() == False
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.click_auto_wait_target()
        assert target_msg == "Target clicked."

    def test_click_editable_nonzero_input(self, apply_time=3):  # Test to click button with editable and nonzero checked in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_button_element_from_settings()
        playground_page.click_visible_checkbox()
        assert playground_page.status_visible_checkbox() == False
        playground_page.click_enabled_checkbox()
        assert playground_page.status_enabled_checkbox() == False
        assert playground_page.status_editable_checkbox() == True
        playground_page.click_ontop_checkbox()
        assert playground_page.status_ontop_checkbox() == False
        assert playground_page.status_nonzero_checkbox() == True
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.click_auto_wait_target()
        assert target_msg == "Target clicked."

    def test_click_enabled_ontop_input(self, apply_time=10):  # Test to click button with editable and on top checked in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_button_element_from_settings()
        playground_page.click_visible_checkbox()
        assert playground_page.status_visible_checkbox() == False
        assert playground_page.status_enabled_checkbox() == True
        playground_page.click_editable_checkbox()
        assert playground_page.status_editable_checkbox() == False
        assert playground_page.status_ontop_checkbox() == True
        playground_page.click_nonzero_checkbox()
        assert playground_page.status_nonzero_checkbox() == False
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.click_auto_wait_target()
        assert target_msg == "Target clicked."

    def test_enter_text_full_input_field(self, apply_time = 3, text = "Testing input"): #Test to enter text in input field with all the properties checked in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_input_element_from_settings()
        assert playground_page.status_visible_checkbox() == True
        assert playground_page.status_enabled_checkbox() == True
        assert playground_page.status_editable_checkbox() == True
        assert playground_page.status_ontop_checkbox() == True
        assert playground_page.status_nonzero_checkbox() == True
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.enter_text_into_target_field(text)
        assert target_msg == f"Text: {text}"

    def test_modify_text_input_field(self, apply_time = 3, text = "Testing input"): #Test to enter text in input field and modify it afterwards with all the properties checked in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_input_element_from_settings()
        assert playground_page.status_visible_checkbox() == True
        assert playground_page.status_enabled_checkbox() == True
        assert playground_page.status_editable_checkbox() == True
        assert playground_page.status_ontop_checkbox() == True
        assert playground_page.status_nonzero_checkbox() == True
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.enter_text_into_target_field(text)
        assert target_msg == f"Text: {text}"
        playground_page.clear_text_in_target_field()
        text = "Testing"
        target_msg = playground_page.enter_text_into_target_field(text)
        assert target_msg == f"Text: {text}"

    def test_enter_text_only_visible_input(self, apply_time=5, text = "Testing input"):  # Test to enter text with only visible checked in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_input_element_from_settings()
        assert playground_page.status_visible_checkbox() == True
        playground_page.click_enabled_checkbox()
        assert playground_page.status_enabled_checkbox() == False
        playground_page.click_editable_checkbox()
        assert playground_page.status_editable_checkbox() == False
        playground_page.click_ontop_checkbox()
        assert playground_page.status_ontop_checkbox() == False
        playground_page.click_nonzero_checkbox()
        assert playground_page.status_nonzero_checkbox() == False
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.enter_text_into_target_field(text)
        assert target_msg == f"Text: {text}"

    def test_enter_text_editable_nonzero_input(self, apply_time=3, text = "Testing input"):  # Test to enter text with editable and nonzero checked in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_input_element_from_settings()
        playground_page.click_visible_checkbox()
        assert playground_page.status_visible_checkbox() == False
        playground_page.click_enabled_checkbox()
        assert playground_page.status_enabled_checkbox() == False
        assert playground_page.status_editable_checkbox() == True
        playground_page.click_ontop_checkbox()
        assert playground_page.status_ontop_checkbox() == False
        assert playground_page.status_nonzero_checkbox() == True
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.enter_text_into_target_field(text)
        assert target_msg == f"Text: {text}"

    def test_enter_text_enabled_ontop_input(self, apply_time=10, text = "Testing input"):  # Test to enter text with editable and on top checked in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_input_element_from_settings()
        playground_page.click_visible_checkbox()
        assert playground_page.status_visible_checkbox() == False
        assert playground_page.status_enabled_checkbox() == True
        playground_page.click_editable_checkbox()
        assert playground_page.status_editable_checkbox() == False
        assert playground_page.status_ontop_checkbox() == True
        playground_page.click_nonzero_checkbox()
        assert playground_page.status_nonzero_checkbox() == False
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.enter_text_into_target_field(text)
        assert target_msg == f"Text: {text}"

    def test_click_full_textarea(self, apply_time = 3): #Test to click input with all the properties checked in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_textarea_element_from_settings()
        assert playground_page.status_visible_checkbox() == True
        assert playground_page.status_enabled_checkbox() == True
        assert playground_page.status_editable_checkbox() == True
        assert playground_page.status_ontop_checkbox() == True
        assert playground_page.status_nonzero_checkbox() == True
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.click_auto_wait_target()
        assert target_msg == "Target clicked."

    def test_click_only_visible_textarea(self, apply_time=5):  # Test to click button with only visible checked in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_textarea_element_from_settings()
        assert playground_page.status_visible_checkbox() == True
        playground_page.click_enabled_checkbox()
        assert playground_page.status_enabled_checkbox() == False
        playground_page.click_editable_checkbox()
        assert playground_page.status_editable_checkbox() == False
        playground_page.click_ontop_checkbox()
        assert playground_page.status_ontop_checkbox() == False
        playground_page.click_nonzero_checkbox()
        assert playground_page.status_nonzero_checkbox() == False
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.click_auto_wait_target()
        assert target_msg == "Target clicked."

    def test_click_editable_nonzero_textarea(self, apply_time=3):  # Test to click button with editable and nonzero checked in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_textarea_element_from_settings()
        playground_page.click_visible_checkbox()
        assert playground_page.status_visible_checkbox() == False
        playground_page.click_enabled_checkbox()
        assert playground_page.status_enabled_checkbox() == False
        assert playground_page.status_editable_checkbox() == True
        playground_page.click_ontop_checkbox()
        assert playground_page.status_ontop_checkbox() == False
        assert playground_page.status_nonzero_checkbox() == True
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.click_auto_wait_target()
        assert target_msg == "Target clicked."

    def test_click_enabled_ontop_textarea(self, apply_time=10):  # Test to click button with editable and on top checked in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_textarea_element_from_settings()
        playground_page.click_visible_checkbox()
        assert playground_page.status_visible_checkbox() == False
        assert playground_page.status_enabled_checkbox() == True
        playground_page.click_editable_checkbox()
        assert playground_page.status_editable_checkbox() == False
        assert playground_page.status_ontop_checkbox() == True
        playground_page.click_nonzero_checkbox()
        assert playground_page.status_nonzero_checkbox() == False
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.click_auto_wait_target()
        assert target_msg == "Target clicked."

    def test_enter_text_full_textarea_field(self, apply_time = 3, text = "Testing input"): #Test to enter text in input field with all the properties checked in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_textarea_element_from_settings()
        assert playground_page.status_visible_checkbox() == True
        assert playground_page.status_enabled_checkbox() == True
        assert playground_page.status_editable_checkbox() == True
        assert playground_page.status_ontop_checkbox() == True
        assert playground_page.status_nonzero_checkbox() == True
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.enter_text_into_target_field(text)
        assert target_msg == f"Text: {text}"

    def test_modify_text_textarea_field(self, apply_time = 3, text = "Testing input"): #Test to enter text in input field and modify it afterwards with all the properties checked in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_textarea_element_from_settings()
        assert playground_page.status_visible_checkbox() == True
        assert playground_page.status_enabled_checkbox() == True
        assert playground_page.status_editable_checkbox() == True
        assert playground_page.status_ontop_checkbox() == True
        assert playground_page.status_nonzero_checkbox() == True
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.enter_text_into_target_field(text)
        assert target_msg == f"Text: {text}"
        playground_page.clear_text_in_target_field()
        text = "Testing"
        target_msg = playground_page.enter_text_into_target_field(text)
        assert target_msg == f"Text: {text}"

    def test_enter_text_only_visible_textarea(self, apply_time=5, text = "Testing input"):  # Test to enter text with only visible checked in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_textarea_element_from_settings()
        assert playground_page.status_visible_checkbox() == True
        playground_page.click_enabled_checkbox()
        assert playground_page.status_enabled_checkbox() == False
        playground_page.click_editable_checkbox()
        assert playground_page.status_editable_checkbox() == False
        playground_page.click_ontop_checkbox()
        assert playground_page.status_ontop_checkbox() == False
        playground_page.click_nonzero_checkbox()
        assert playground_page.status_nonzero_checkbox() == False
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.enter_text_into_target_field(text)
        assert target_msg == f"Text: {text}"

    def test_enter_text_editable_nonzero_textarea(self, apply_time=3, text = "Testing input"):  # Test to enter text with editable and nonzero checked in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_textarea_element_from_settings()
        playground_page.click_visible_checkbox()
        assert playground_page.status_visible_checkbox() == False
        playground_page.click_enabled_checkbox()
        assert playground_page.status_enabled_checkbox() == False
        assert playground_page.status_editable_checkbox() == True
        playground_page.click_ontop_checkbox()
        assert playground_page.status_ontop_checkbox() == False
        assert playground_page.status_nonzero_checkbox() == True
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.enter_text_into_target_field(text)
        assert target_msg == f"Text: {text}"

    def test_enter_text_enabled_ontop_textarea(self, apply_time=10, text = "Testing input"):  # Test to enter text with editable and on top checked in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_textarea_element_from_settings()
        playground_page.click_visible_checkbox()
        assert playground_page.status_visible_checkbox() == False
        assert playground_page.status_enabled_checkbox() == True
        playground_page.click_editable_checkbox()
        assert playground_page.status_editable_checkbox() == False
        assert playground_page.status_ontop_checkbox() == True
        playground_page.click_nonzero_checkbox()
        assert playground_page.status_nonzero_checkbox() == False
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.enter_text_into_target_field(text)
        assert target_msg == f"Text: {text}"

    def test_click_full_select_target(self, apply_time = 3): #Test to click select with all the properties checked in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_select_element_from_settings()
        assert playground_page.status_visible_checkbox() == True
        assert playground_page.status_enabled_checkbox() == True
        assert playground_page.status_editable_checkbox() == True
        assert playground_page.status_ontop_checkbox() == True
        assert playground_page.status_nonzero_checkbox() == True
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.click_auto_wait_target()
        assert target_msg == "Target clicked."

    def test_select_full_item1(self, apply_time = 5, item = 1): #Test to select Item 1 with all the properties checked from target dropdown in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_select_element_from_settings()
        assert playground_page.status_visible_checkbox() == True
        assert playground_page.status_enabled_checkbox() == True
        assert playground_page.status_editable_checkbox() == True
        assert playground_page.status_ontop_checkbox() == True
        assert playground_page.status_nonzero_checkbox() == True
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.select_target_dropdown(item)
        assert target_msg == f"Selected: Item {item}"

    def test_select_only_visible_item1(self, apply_time = 3, item = 1): #Test to select Item 1 with only visible property checked from target dropdown in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_select_element_from_settings()
        assert playground_page.status_visible_checkbox() == True
        playground_page.click_enabled_checkbox()
        assert playground_page.status_enabled_checkbox() == False
        playground_page.click_editable_checkbox()
        assert playground_page.status_editable_checkbox() == False
        playground_page.click_ontop_checkbox()
        assert playground_page.status_ontop_checkbox() == False
        playground_page.click_nonzero_checkbox()
        assert playground_page.status_nonzero_checkbox() == False
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.select_target_dropdown(item)
        assert target_msg == f"Selected: Item {item}"

    def test_select_editable_nonzero_item1(self, apply_time = 10, item = 1): #Test to select Item 1 with editable and non zero properties checked from target dropdown in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_select_element_from_settings()
        playground_page.click_visible_checkbox()
        assert playground_page.status_visible_checkbox() == False
        playground_page.click_enabled_checkbox()
        assert playground_page.status_enabled_checkbox() == False
        assert playground_page.status_editable_checkbox() == True
        playground_page.click_ontop_checkbox()
        assert playground_page.status_ontop_checkbox() == False
        assert playground_page.status_nonzero_checkbox() == True
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.select_target_dropdown(item)
        assert target_msg == f"Selected: Item {item}"

    def test_select_enabled_ontop_item1(self, apply_time = 5, item = 1): #Test to select Item 1 with enabled and on top properties checked from target dropdown in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_select_element_from_settings()
        playground_page.click_visible_checkbox()
        assert playground_page.status_visible_checkbox() == False
        assert playground_page.status_enabled_checkbox() == True
        playground_page.click_editable_checkbox()
        assert playground_page.status_editable_checkbox() == False
        assert playground_page.status_ontop_checkbox() == True
        playground_page.click_nonzero_checkbox()
        assert playground_page.status_nonzero_checkbox() == False
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.select_target_dropdown(item)
        assert target_msg == f"Selected: Item {item}"

    def test_select_full_item2(self, apply_time = 3, item = 2): #Test to select Item 2 with all the properties checked from target dropdown in Auto Wait page        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_select_element_from_settings()
        assert playground_page.status_visible_checkbox() == True
        assert playground_page.status_enabled_checkbox() == True
        assert playground_page.status_editable_checkbox() == True
        assert playground_page.status_ontop_checkbox() == True
        assert playground_page.status_nonzero_checkbox() == True
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.select_target_dropdown(item)
        assert target_msg == f"Selected: Item {item}"

    def test_select_only_visible_item2(self, apply_time = 3, item = 2): #Test to select Item 2 with only visible property checked from target dropdown in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_select_element_from_settings()
        assert playground_page.status_visible_checkbox() == True
        playground_page.click_enabled_checkbox()
        assert playground_page.status_enabled_checkbox() == False
        playground_page.click_editable_checkbox()
        assert playground_page.status_editable_checkbox() == False
        playground_page.click_ontop_checkbox()
        assert playground_page.status_ontop_checkbox() == False
        playground_page.click_nonzero_checkbox()
        assert playground_page.status_nonzero_checkbox() == False
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.select_target_dropdown(item)
        assert target_msg == f"Selected: Item {item}"

    def test_select_editable_nonzero_item2(self, apply_time = 10, item = 2): #Test to select Item 2 with editable and non zero properties checked from target dropdown in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_select_element_from_settings()
        playground_page.click_visible_checkbox()
        assert playground_page.status_visible_checkbox() == False
        playground_page.click_enabled_checkbox()
        assert playground_page.status_enabled_checkbox() == False
        assert playground_page.status_editable_checkbox() == True
        playground_page.click_ontop_checkbox()
        assert playground_page.status_ontop_checkbox() == False
        assert playground_page.status_nonzero_checkbox() == True
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.select_target_dropdown(item)
        assert target_msg == f"Selected: Item {item}"

    def test_select_enabled_ontop_item2(self, apply_time = 5, item = 2): #Test to select Item 2 with enabled and on top properties checked from target dropdown in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_select_element_from_settings()
        playground_page.click_visible_checkbox()
        assert playground_page.status_visible_checkbox() == False
        assert playground_page.status_enabled_checkbox() == True
        playground_page.click_editable_checkbox()
        assert playground_page.status_editable_checkbox() == False
        assert playground_page.status_ontop_checkbox() == True
        playground_page.click_nonzero_checkbox()
        assert playground_page.status_nonzero_checkbox() == False
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.select_target_dropdown(item)
        assert target_msg == f"Selected: Item {item}"

    def test_select_full_item3(self, apply_time = 10, item = 3): #Test to select Item 3 with all the properties checked from target dropdown in Auto Wait page        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_select_element_from_settings()
        assert playground_page.status_visible_checkbox() == True
        assert playground_page.status_enabled_checkbox() == True
        assert playground_page.status_editable_checkbox() == True
        assert playground_page.status_ontop_checkbox() == True
        assert playground_page.status_nonzero_checkbox() == True
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.select_target_dropdown(item)
        assert target_msg == f"Selected: Item {item}"

    def test_select_only_visible_item3(self, apply_time = 5, item = 3): #Test to select Item 3 with only visible property checked from target dropdown in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_select_element_from_settings()
        assert playground_page.status_visible_checkbox() == True
        playground_page.click_enabled_checkbox()
        assert playground_page.status_enabled_checkbox() == False
        playground_page.click_editable_checkbox()
        assert playground_page.status_editable_checkbox() == False
        playground_page.click_ontop_checkbox()
        assert playground_page.status_ontop_checkbox() == False
        playground_page.click_nonzero_checkbox()
        assert playground_page.status_nonzero_checkbox() == False
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.select_target_dropdown(item)
        assert target_msg == f"Selected: Item {item}"

    def test_select_editable_nonzero_item3(self, apply_time = 10, item = 3): #Test to select Item 3 with editable and non zero properties checked from target dropdown in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_select_element_from_settings()
        playground_page.click_visible_checkbox()
        assert playground_page.status_visible_checkbox() == False
        playground_page.click_enabled_checkbox()
        assert playground_page.status_enabled_checkbox() == False
        assert playground_page.status_editable_checkbox() == True
        playground_page.click_ontop_checkbox()
        assert playground_page.status_ontop_checkbox() == False
        assert playground_page.status_nonzero_checkbox() == True
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.select_target_dropdown(item)
        assert target_msg == f"Selected: Item {item}"

    def test_select_enabled_ontop_item3(self, apply_time = 3, item = 3): #Test to select Item 3 with enabled and on top properties checked from target dropdown in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_select_element_from_settings()
        playground_page.click_visible_checkbox()
        assert playground_page.status_visible_checkbox() == False
        assert playground_page.status_enabled_checkbox() == True
        playground_page.click_editable_checkbox()
        assert playground_page.status_editable_checkbox() == False
        assert playground_page.status_ontop_checkbox() == True
        playground_page.click_nonzero_checkbox()
        assert playground_page.status_nonzero_checkbox() == False
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.select_target_dropdown(item)
        assert target_msg == f"Selected: Item {item}"

    def test_click_full_label(self, apply_time = 3): #Test to click label with all the properties checked in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_label_element_from_settings()
        assert playground_page.status_visible_checkbox() == True
        assert playground_page.status_enabled_checkbox() == True
        assert playground_page.status_editable_checkbox() == True
        assert playground_page.status_ontop_checkbox() == True
        assert playground_page.status_nonzero_checkbox() == True
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.click_auto_wait_target()
        assert target_msg == "Target clicked."

    def test_click_only_visible_label(self, apply_time=5):  # Test to click label with only visible checked in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_label_element_from_settings()
        assert playground_page.status_visible_checkbox() == True
        playground_page.click_enabled_checkbox()
        assert playground_page.status_enabled_checkbox() == False
        playground_page.click_editable_checkbox()
        assert playground_page.status_editable_checkbox() == False
        playground_page.click_ontop_checkbox()
        assert playground_page.status_ontop_checkbox() == False
        playground_page.click_nonzero_checkbox()
        assert playground_page.status_nonzero_checkbox() == False
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.click_auto_wait_target()
        assert target_msg == "Target clicked."

    def test_click_editable_nonzero_label(self, apply_time=5):  # Test to click label with editable and nonzero checked in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_label_element_from_settings()
        playground_page.click_visible_checkbox()
        assert playground_page.status_visible_checkbox() == False
        playground_page.click_enabled_checkbox()
        assert playground_page.status_enabled_checkbox() == False
        assert playground_page.status_editable_checkbox() == True
        playground_page.click_ontop_checkbox()
        assert playground_page.status_ontop_checkbox() == False
        assert playground_page.status_nonzero_checkbox() == True
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.click_auto_wait_target()
        assert target_msg == "Target clicked."

    def test_click_enabled_ontop_label(self, apply_time=10):  # Test to click label with editable and on top checked in Auto Wait page
        self.driver.get(data.automation_playground_url + data.auto_wait_url)
        playground_page = UITestingPlayground(self.driver)
        playground_page.select_label_element_from_settings()
        playground_page.click_visible_checkbox()
        assert playground_page.status_visible_checkbox() == False
        assert playground_page.status_enabled_checkbox() == True
        playground_page.click_editable_checkbox()
        assert playground_page.status_editable_checkbox() == False
        assert playground_page.status_ontop_checkbox() == True
        playground_page.click_nonzero_checkbox()
        assert playground_page.status_nonzero_checkbox() == False
        if apply_time == 3:
            apply_msg = playground_page.click_apply_3s_button()
            assert apply_msg == "Target element settings applied for 3 seconds."
        elif apply_time == 5:
            apply_msg = playground_page.click_apply_5s_button()
            assert apply_msg == "Target element settings applied for 5 seconds."
        elif apply_time == 10:
            apply_msg = playground_page.click_apply_10s_button()
            assert apply_msg == "Target element settings applied for 10 seconds."
        target_msg = playground_page.click_auto_wait_target()
        assert target_msg == "Target clicked."


    @classmethod
    def teardown_class(cls): #Closes the browser
        cls.driver.quit()