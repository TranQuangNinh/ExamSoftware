// Disable Right Click
// var isNS = (navigator.appName == "Netscape") ? 1 : 0;

// if (navigator.appName == "Netscape") document.captureEvents(Event.MOUSEDOWN || Event.MOUSEUP);

// function mischandler() {
//     return false;
// }

// function mousehandler(e) {
//     var myevent = (isNS) ? e : event;
//     var eventbutton = (isNS) ? myevent.which : myevent.button;
//     if ((eventbutton == 2) || (eventbutton == 3)) return false;
// }
// document.oncontextmenu = mischandler;
// document.onmousedown = mousehandler;
// document.onmouseup = mousehandler;

document.onkeydown = function (e) {
    if (event.keyCode == 123) {
        return false;
    }
    if (e.ctrlKey && e.shiftKey && e.keyCode == 'I'.charCodeAt(0)) {
        return false;
    }
    if (e.ctrlKey && e.shiftKey && e.keyCode == 'J'.charCodeAt(0)) {
        return false;
    }
    if (e.ctrlKey && e.keyCode == 'U'.charCodeAt(0)) {
        return false;
    }
}