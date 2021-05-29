console.log('hello world from main')

const postBox = document.getElementById('posts-box')
const prodCol = document.getElementById('coluna-produto')
const precoCol = document.getElementById('coluna-preco')
const spinnerBox = document.getElementById('spinner-box')
const loadBtn = document.getElementById('load-btn')
const loadBox = document.getElementById('loading-box')
let visible = 16

const handleGetData = () => {
    $.ajax({
        type:'GET',
        url: `/newresult/${visible}/`,
        success: function(response){
//            console.log(response.max)
           maxSize = response.max
            const data = response.data
            setTimeout(()=>{
                data.map(post=>{
                    console.log(post.product)
                    postBox.innerHTML +=    `<div class="col-lg-3 col-md-4 col-sm-5 pb-2">
                                            <div class="card border-0">
                                            <img class="card-img-top" src=${post.image} alt="Card image cap">
                                            <div class="card-body">
                                            <h9 class="card-title text-warning font-weight-bold" id="coluna-produto">${post.product}</h9>
                                            <p class="card-text" id="coluna-preco">${post.price}</p>
                                            <a href=${post.link} target="_blank" class="btn btn-warning">See more</a>
                                            </div>
                                            </div>
                                            </div>`
                })
            }, 500)

            if(maxSize){
                    setTimeout(function(){
                    loadBox.innerHTML = `<h4>No more results to be loaded.</h4>`
                    console.log(loadBox)
                    }, 1000);
            }
        },
        error: function(error){
            console.log(error)
        }
    })
}

handleGetData()
loadBtn.addEventListener('click', ()=>{
    visible += 16
    handleGetData()
})