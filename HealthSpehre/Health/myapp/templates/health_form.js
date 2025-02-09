function storeData() {
    // Get values from the form
    const age = document.getElementById('age').value;
    const height = document.getElementById('height').value;
    const weight = document.getElementById('weight').value;
    
    // Get selected gender
    const gender = document.querySelector('input[name="gender"]:checked')?.id || '';

    // Store values in localStorage
    localStorage.setItem('age', age);
    localStorage.setItem('gender', gender);
    localStorage.setItem('height', height);
    localStorage.setItem('weight', weight);

    // Optionally alert the user
    alert("Data Stored Successfully!");
}