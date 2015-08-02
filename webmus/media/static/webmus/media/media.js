(function() {
    var handle_youtube = function(width, height, item) {
        var text = item.text();
        var embed = '//www.youtube.com/embed/' + item.data('key');
        var thumb = $(
            '<a class="video-embed" href="' + embed + '" style="background-image: url(' + item.data('thumbnail') + ');"></a>')
        var par = item.parent().parent();

        thumb.click(function(ev) {
            ev.preventDefault();
            $.colorbox({
                href: thumb.attr('href'),
                iframe: true,
                innerWidth: par.width(),
                innerHeight: par.width() * 0.61
            });
        });

        thumb.append($('<span>' + text + '</span>'));
        item.replaceWith(thumb);
    };

    var handle_vimeo = function(width, height, item) {
        var iframe = $(
            '<iframe width="' + width + '" height="' + height +
            '" src="//player.vimeo.com/video/' + item.data('key') +
            '" frameborder="0" allowfullscreen></iframe>');
        item.replaceWith(iframe);
    };

    var handle_soundcloud = function(width, height, item) {
        var embed_url = '//soundcloud.com/oembed?format=json' +
                        '&maxwidth=' + width + '&maxheight=' + height +
                        '&url=' + item.attr('href');
        var success = function(json) {
            var iframe = $(json.html);
            item.replaceWith(iframe);
        };
        $.ajax({url: embed_url, success: success});
    };

    var handlers = {
        'youtube': handle_youtube,
        'vimeo': handle_vimeo,
        'soundcloud': handle_soundcloud
    };

    function do_media_embed() {
        $('.media-item a').each(function(i, item) {
            item = $(item);
            var source = item.data('source');
            var handler = handlers[source];

            if (handler == undefined) {
                console.log("No handler for " + source);
            } else {
                // TODO; work with thumbnails so only do the iframe embed
                // once the thumb has been clicked
                var width = item.parent().width();
                var height = item.parent().height();
                handler(width, height, item);
            }
        });
    };

    $(function() {
        do_media_embed();    
    });
}());
