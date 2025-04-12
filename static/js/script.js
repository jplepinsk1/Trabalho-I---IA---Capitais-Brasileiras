document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const select_origem = form.querySelector('select[name="origem"]');
        const select_destino = form.querySelector('select[name="destino"]');
        if (select_destino.value === select_origem.value) {
            alert('Por favor, O campo de origem e destino não podem ser iguais!');
            select_origem.focus();
            return;
        }

        form.submit();
    });
});
