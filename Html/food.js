<script>
    function togglePassword() {
        const passwordField = document.getElementById('password');
        const toggleIcon = document.querySelector('.toggle-password');
        if (passwordField.type === 'password') {
            passwordField.type = 'text';
            toggleIcon.innerHTML = '&#128068;'; // Change icon if desired
        } else {
            passwordField.type = 'password';
            toggleIcon.innerHTML = '&#128065;';
        }
    }
</script>
