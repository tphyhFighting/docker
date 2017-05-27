$(document).ready(function () {
  console.log("ready");
   $(".search-form").submit(function(e){
     console.log("search form");
     console.log("id:",$("#id").val());
     // 2. This code loads the IFrame Player API code asynchronously.
      var tag = document.createElement('script');
      tag.src = "https://www.youtube.com/iframe_api";
      var firstScriptTag = document.getElementsByTagName('script')[0];
     console.log(firstScriptTag)
      firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

      // 3. This function creates an <iframe> (and YouTube player)
      //    after the API code downloads.
    var videoId = $("#id").val();
      var player;
      console.log("vidoeid:", videoId);
      function onYouTubeIframeAPIReady() {
        player = new YT.Player('player', {
          height: '360',
          width: '640',
          videoId: videoId,
          events: {
            'onReady': onPlayerReady1,
            'onStateChange': onPlayerStateChange1
          }
        });

        // 4. The API will call this function when the video player is ready.
       function onPlayerReady1(event) {
         console.log("onplayerReady")
         event.target.playVideo();
       }

       // 5. The API calls this function when the player's state changes.
      //    The function indicates that when playing a video (state=1),
      //    the player should play for six seconds and then stop.
      var done = false;
      function onPlayerStateChange1(event) {
        if (event.data == YT.PlayerState.PLAYING && !done) {
          setTimeout(stopVideo, 6000);
          done = true;
        }
      }
      function stopVideo() {
        player.stopVideo();
      }
      }

   });
});
