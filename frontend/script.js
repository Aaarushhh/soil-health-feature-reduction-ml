// document.getElementById("predictForm").addEventListener("submit", async (event) => {
//   event.preventDefault();

//   const data = {
//     State: document.getElementById("State").value,
//     District: document.getElementById("District").value,
//     Farmer_ID: document.getElementById("Farmer_ID").value,
//     Soil_Type: document.getElementById("Soil_Type").value,
//     pH: parseFloat(document.getElementById("pH").value),
//     EC: parseFloat(document.getElementById("EC").value),
//     OC: parseFloat(document.getElementById("OC").value),
//     N: parseInt(document.getElementById("N").value),
//     P: parseInt(document.getElementById("P").value),
//     K: parseInt(document.getElementById("K").value),
//     Moisture: parseFloat(document.getElementById("Moisture").value),
//   };

//   try {
//     const response = await fetch("http://127.0.0.1:5000/predict", {
//       method: "POST",
//       headers: { "Content-Type": "application/json" },
//       body: JSON.stringify(data),
//     });

//     const result = await response.json();
//     if (result.status === "success") {
//       document.getElementById("result").innerText =
//         "✅ Predicted Crop Suitability: " + result.predicted_crop_suitability;
//     } else {
//       document.getElementById("result").innerText =
//         "⚠️ Error: " + result.message;
//     }
//   } catch (error) {
//     document.getElementById("result").innerText = "❌ Server error: " + error;
//   }
// });
