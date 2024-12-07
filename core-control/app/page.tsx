"use client";
import React, { useState } from "react";

const Base64ToImage = () => {
  const [base64String, setBase64String] = useState("");
  const [imageUrl, setImageUrl] = useState("");

  const handleInputChange = (e) => {
    setBase64String(e.target.value);
  };

  const convertToImage = () => {
    if (!base64String) {
      alert("Please enter a valid Base64 string");
      return;
    }

    // Create a data URL from the Base64 string
    const dataUrl = `data:image/png;base64,${base64String}`;
    setImageUrl(dataUrl); // Set the image URL for display
  };

  return (
    <div>
      <h1>Base64 to Image</h1>
      <textarea
        rows="5"
        cols="50"
        placeholder="Enter Base64 string here"
        value={base64String}
        onChange={handleInputChange}
      />
      <br />
      <button onClick={convertToImage}>Convert to Image</button>
      <br />
      {imageUrl && (
        <div>
          <h3>Converted Image:</h3>
          <img src={imageUrl} alt="Converted" style={{ maxWidth: "100%" }} />
          <br />
          <a href={imageUrl} download="converted_image.png">
            Download Image
          </a>
        </div>
      )}
    </div>
  );
};

export default Base64ToImage;
