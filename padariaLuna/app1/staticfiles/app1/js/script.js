function mostrarCategoria(categoria) {
    esconderTodasCategorias();

    var categoriaSelecionada = document.getElementById(categoria);
    categoriaSelecionada.style.display = "block";
}

function esconderTodasCategorias() {
    console.log('escondendo categorias');
    var categorias = document.querySelectorAll("#categorias > div");
    categorias.forEach(function(c) {
        c.style.display = "none";
    });
}

function inicio() {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    const totalValor = document.getElementById("total-valor");
    
    checkboxes.forEach(function(checkbox) {
        checkbox.addEventListener("change", function() {
            let total = 0;
    
            checkboxes.forEach(function(checkbox) {
                if (checkbox.checked) {
                    total += parseFloat(checkbox.value.split(" - $")[1]);
                }
            });
        
            totalValor.textContent = "$" + total.toFixed(2);
        });
    });

    const switchModal = () => {
        const modal = document.querySelector('.modal')
        const actualStyle = modal.style.display
        if(actualStyle == 'block') {
          modal.style.display = 'none'
        }
        else {
          modal.style.display = 'block'
        }
      }
      
      const btn = document.querySelector('.modalBtn')
      btn.addEventListener('click', switchModal)
      
      window.onclick = function(event) {
          const modal = document.querySelector('.modal')
        if (event.target == modal) {
          switchModal()
        }
      }
    
    const confirmarPedidoButton = document.getElementById("confirmar-pedido");
    confirmarPedidoButton.addEventListener("click", function() {

        const paragrafo = document.getElementById('texto-modal');

        paragrafo.innerHTML = `Pedido confirmado!<br>Valor: ${totalValor.textContent}.<br>Número do pedido: ${Math.trunc(Math.random()*1000)}.`;
        switchModal(`Pedido confirmado!\nValor: ${totalValor.textContent}.\nNúmero do pedido: ${Math.trunc(Math.random()*1000)}.`);
    
        
    });
    
    esconderTodasCategorias();
}

document.addEventListener("DOMContentLoaded", inicio, false);