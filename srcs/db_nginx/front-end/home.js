
/***window scrool */
window.addEventListener('scroll',function(){
    var header = document.querySelector('header');
    header.classList.toggle('sticky',window.scrollY > 0);
});


/**** coalition rank** */

let t1 = document.getElementById("coalFirst");
let t2= document.getElementById("coalSecond");
let t3 = document.getElementById("coalThird");

/**tournament box  */

var swiper = new Swiper(".swiper-container", {
    effect: "cards",
    grabCursor: true,
    initialSlide: 2,
    speed: 500,
    loop: true,
    rotate: true,
    mousewheel: {
        invert: false,
    },
});


/***  STatistics 
   chart 1*/

   const ctx = document.getElementById('myChart').getContext('2d');

   const doughnut =  new Chart(ctx, {
      type: 'doughnut',
      data: {
        labels: ['Vs.Friend', 'Vs.AI', 'VS.unkown', 'Tournament'],
        datasets: [{
          label: 'Match Statistics Overview',
          data: [12, 19, 3, 5,],
          backgroundColor:
          [
            'rgba(255,99,132,0.2)',
            'rgba(54,162,235,0.2)',
            'rgba(255,206,86,0.2)',
            'rgba(75,192,192,0.2)',
           
          ],
          borderColor:[
            'rgba(255,99,132,1)',
            'rgba(54,162,235,1)',
            'rgba(255,206,86,1)',
            'rgba(75,192,192,1)',
            'rgba(135,102,255,1)',
            'rgba(255,159,64,1)',
          ],
          borderWidth: 1
        }]
      },
      options: {
        plugins: {
          legend: {
              labels: {
                  color: 'white',
                  font: {
                      size: 10,
                      weight: 'bold'
                  }
              }
          }},
        datalabels: {
          color: 'white', // Set the color of the data labels
          font: {
              size: 16,
              weight: 'bold'
          }},
        scales: {
          y: {
            beginAtZero: true,
            ticks :{
              color : 'white'
            }
          }
        }
      }
    });


    const mycoali = document.getElementById('piechart').getContext('2d');
    let chart = new Chart(mycoali, {
        type: 'pie',
        data: {
            labels: ['Freax', 'Comodore', 'Bios', 'Pandora'],
            datasets: [{
                data: [102, 36, 12, 5],
                backgroundColor: [
                    'rgba(255, 204, 0, 0.6)', 
                    'rgba(0, 128, 0, 0.5)',   
                    'rgba(135,206,250,0.7)',
                    'rgba(255, 20, 147, 0.6)' 
                ],
                borderColor: [
                    'rgba(255, 204, 0, 1)',   
                    'rgba(0, 128, 0, 1)',     
                    'rgba(135,206,250,1)',     
                    'rgba(255, 20, 147, .9)'   
                ],
                borderWidth: 2,
                hoverBorderWidth: 4
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    labels: {
                        color: 'white',
                        font: {
                            size: 12,
                            weight: 'bold'
                        }
                    },
                    position: 'top',
                    display: true
                }
            }
        }
    });