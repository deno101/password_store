function generateRandom(len = 12) {
    let chars = "QWERTYUIOPLKJHGFDSAZXCVBNMlkjhgfdsaqwertyuiopmnbvcxz1234567890!@#$%^&*{}:?></.,;[]-_"
    let result = ""
    for (let i = 0; i < len; i++) {
        result += chars.charAt(Math.floor(Math.random() * chars.length))
    }
    return result
}

$(document).ready(function (){
    $('#random').click(function () {
        $('#password').val(generateRandom())
    })
})