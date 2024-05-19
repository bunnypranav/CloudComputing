$(function () {
  var syncClient;
  var syncStream;
  var text_area = document.getElementById("text_area");
  var select_element = document.getElementById("select");
  var background_color;

  $.getJSON("/token", function (tokenResponse) {
    syncClient = new Twilio.Sync.Client(tokenResponse.token, {
      logLevel: "info",
    });

    // create the stream object
    syncClient.stream("messageData").then(function (stream) {
      syncStream = stream;
      // listen update and sync drawing data
      syncStream.on("messagePublished", function (event) {
        console.log("syncStream:", event.message.value);
        syncDrawingData(event.message.value);
      });
    });
  });
});
