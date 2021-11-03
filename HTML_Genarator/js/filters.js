class Form{
    div= ''
    constructor(){
        this.on_init()
        this.form=document.querySelector(this.div)
        this.series_serach=document.querySelector(this.div_series)
    }

    set_form(data){
        this.set_series(data)
    }

    set_series(data){
        function if_exist(name,array){
            let count=0
            for (let index of array){
                if (index === name){
                    count++
                }
            }
            return count
        }
        let array=[]
        for (let el of data){
            if (!if_exist(el['short_series'].name,array)) { 
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
    }

    html(){
        let form ='<input type="text" class="form-control" placeholder="First name" aria-label="First name">'
        return form
        
    }

}
