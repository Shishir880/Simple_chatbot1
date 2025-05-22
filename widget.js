



(function () {
  const iframe = document.createElement("iframe");
  iframe.src = "http://127.0.0.1:5000/chat";  // তোমার ডোমেইন বা IP দিবো পরে
  iframe.style = "position:fixed;bottom:20px;right:20px;width:350px;height:500px;border:none;z-index:9999;";
  document.body.appendChild(iframe);
})();
