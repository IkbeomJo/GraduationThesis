function dispatchClickEvent(selector) {
    const element = document.querySelector(selector);
    if (element) {
      element.click(); // 클릭 이벤트 발생
      console.log(selector + " 요소를 클릭했습니다.");
    } else {
      console.log("해당 요소를 찾을 수 없습니다.");
    }
  };

function selectComboBoxOption(selector, optionValue) {
    const element = document.querySelector(selector);
    if (element) {
      element.value = optionValue; // 입력받은 값으로 콤보박스를 선택
      console.log(selector + " 콤보박스를 " + optionValue + "로 선택했습니다.");
    } else {
      console.log("해당 요소를 찾을 수 없습니다.");
    }
}
  
function setSpinBoxValue(selector, value) {
    const element = document.querySelector(selector + " input[type=text]");
    if (element) {
      element.value = value;
      console.log(selector + " 스핀박스의 값을 " + value + "으로 변경했습니다.");
    } else {
      console.log("해당 요소를 찾을 수 없습니다.");
    }
  }
  
dispatchClickEvent("#mainframe\\.HFrameSet00\\.LeftFrame\\.form\\.div_left_wrap2\\.form\\.menulist_wrap\\.form\\.menu_dep02_wrap_1\\.form\\.menu_dep03_wrap_1\\.form\\.menu_dep04_wrap_1\\.form\\.menu_dep04_14");

setSpinBoxValue("#mainframe\\.HFrameSet00\\.VFrameSet00\\.WorkFrame\\.2429\\.form\\.div_content\\.form\\.div_search\\.form\\.spn_shyr\\.spinedit", "2023");

selectComboBoxOption("#mainframe\\.HFrameSet00\\.VFrameSet00\\.WorkFrame\\.2429\\.form\\.div_content\\.form\\.div_search\\.form\\.cbo_smstGbcd .nexainput", "2학기");

dispatchClickEvent("#mainframe\\.HFrameSet00\\.VFrameSet00\\.WorkFrame\\.2429\\.form\\.div_content\\.form\\.div_search\\.form\\.btn_search");
