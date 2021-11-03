class Form{
    div= ''
    constructor(){
        this.on_init()
        this.form=document.querySelector(this.div)
        this.series_serach=document.querySelector(this.div_series)
        this.producent_serach=document.querySelector(this.div_producets)
    }

    if_exist(name,array){
        let count=0
        for (let index of array){
            if (index === name){
                count++
            }
        }
        return count
    }

    set_form(data){
        this.set_series(data)
        this.set_producent(data)
    }

    set_producent(data){
        let array=[]
        for (let el of data){
            if (!this.if_exist(el['producent'].name,array) && el['producent'].name!==undefined) { 
                array.push(el['producent'].name)
            }
        }
        
        for (let option of array){
            this.producent_serach.innerHTML+='<option value="'+option+'">'+option+'</option>'
        }
    }

    set_series(data){
        let array=[]
        for (let el of data){
            if (!this.if_exist(el['short_series'].name,array)) { 
                array.push(el['short_series'].name)
            }
        }
        
        for (let option of array){
            this.series_serach.innerHTML+='<option value="'+option+'">'+option+'</option>'
        }
    }
    
    return_form(){
        return this.form.innerHTML=this.html()
    }
}

class FilterMovies extends Form{ 

    on_init(){
        this.div='.movies-filter'
        this.div_series='.series-search'
        this.div_producets='.producent-search'
    }

    html(){
        let form ='<input type="text" class="form-control" placeholder="First name" aria-label="First name">'
        return form
    }

}
