function hideKedroVizSideBar() {
  var classNm =
    "pipeline-menu-button pipeline-menu-button--menu pipeline-icon-toolbar__button";
  sidebarButtons = document.getElementsByClassName(classNm);
  if (sidebarButtons.length > 0) {
    if (sidebarButtons[0].hasAttribute("aria-label")) {
      if (sidebarButtons[0].ariaLabel == "Hide menu") {
        sidebarButtons[0].click();
      }
    }
  }
}
