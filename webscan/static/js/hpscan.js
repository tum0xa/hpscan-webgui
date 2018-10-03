$('#scan').click(function(){
    Send();
});

function Send() {
    modes = $('#inputGroupColorMode')[0];
        mode = $.each(modes, function(){
        if ($(this).selected == 'true')
            return $(this).value
    }).value;

    res = $('#inputResolution')[0].value;

    // alert(mode + res);

    $.ajax({
        type: 'GET',
        url: '/hpscan/scan',
        data: {'mode': mode,
                'res': res,
        },
        success: function(data){
                $('#scan')[0].disabled='true';
        },
    });
    return false;  
}