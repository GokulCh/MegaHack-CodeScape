function uploadToImgur() {
    const fileInput = document.getElementById('fileInput');
    const previewImage = document.getElementById('previewImage');

    const file = fileInput.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function (e) {
        previewImage.src = e.target.result;
        previewImage.style.display = 'block';

        const imgurClientId = 'fde91f6f2d3ab8b';

        const formData = new FormData();
        formData.append('image', file);

        fetch('https://api.imgur.com/3/image', {
          method: 'POST',
          headers: {
            Authorization: `Client-ID ${imgurClientId}`,
          },
          body: formData,
        })
          .then(response => response.json())
          .then(data => {
            // Handle the Imgur API response here
            alert(data.data.link)
            console.log('Imgur API Response:', data.data.link)
          })
          .catch(error => console.error('Error uploading to Imgur:', error));
      };
      reader.readAsDataURL(file);
    } else {
      alert('Please select an image before uploading.');
    }
  }