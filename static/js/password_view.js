$(document).ready(function () {
    // add listener for copy image
    $('.copy_image').click(function () {
        let input = $(this.parentNode).find('input');
        let range = document.createRange()
        input[0].disabled = false
        input.focus().select()

        try {
            document.execCommand('copy');
        } catch (err) {
            console.log('Oops, unable to copy');
        }
        window.getSelection().removeAllRanges();
        input.blur()
        input[0].disabled = true
    })
})