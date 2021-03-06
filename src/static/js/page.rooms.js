$(document).ready(function(){
    var pageLoadEvent, setUI, bindEvents;
    pageLoadEvent = function(){
        setUI();
        bindEvents();
    };

    setUI = function(){

    };

    bindEvents = function(){
        // remove old content loaded in modal dialog
        // Thanks to http://stackoverflow.com/a/18134067/553073
        $('body').on('hidden.bs.modal', '.modal', function () {
            $(this).removeData('bs.modal');

            // close socket
            if (page && page.room && page.room.socket){
                page.room.socket.close();    
                page.room.socket = undefined;
            }
        });

        $('.nav button.action.changeUser').on('click',function(){
            $.removeCookie('name');
            $.removeCookie('identity');
            window.location.href='/';
        });
    };

    (function(){
        pageLoadEvent();

    })();
});
