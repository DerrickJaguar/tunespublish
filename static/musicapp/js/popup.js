document.addEventListener("songPlaying", (event) => {
    const nextSongId = event.detail.songId;
    if (nextSongId) {
      // Populate the popup with the next song
      const popup = document.getElementById("popup");
      const songTitle = document.getElementById("song-title");
      songTitle.textContent = `Now playing: ${nextSongId}`;
      // Add other song details to the popup as needed
  
      // Show the popup window
      popup.style.display = "block";
  
      // Hide the popup after 10 seconds
      setTimeout(() => {
        popup.style.display = "none";
      }, 10000); // 10 seconds
    }
  });