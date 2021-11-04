class Form{
    div= ''
    constructor(filter){
        this.filter=filter
        this.on_init()
        this.form=document.querySelector(this.div)
        this.series_serach=document.querySelector(this.div_series)
        this.producent_serach=document.querySelector(this.div_producets)
        this.stars_serach=document.querySelector(this.div_stars)
        this.tag_serach=document.querySelector(this.div_tag)
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

    set_tag(data){
        let array=[]
        this.tag_serach.innerHTML='<option selected>Select Tag</option>'
        if (this.filter.hasOwnProperty('producent')){
            this.tag_serach.innerHTML='<option selected>'+this.filter['Tag']+'</option>'
        }
        for (let el of data){
            for (let tag of el['tags']){
                if (!this.if_exist(tag.name,array) && tag.name!==undefined) { 
                    array.push(tag.name)
                }
            }
        }

        for (let option of array){
            
            this.tag_serach.innerHTML+='<option value="'+option+'">'+option+'</option>'
        }
    }

    set_stars(data){
        this.stars_serach.innerHTML='<option selected>Select Star</option>'
        if (this.filter.hasOwnProperty('star')){
            this.stars_serach.innerHTML='<option selected>'+this.filter['star']+'</option>'
        }
        let array=[]
        for (let el of data){
            for (let star of el['short_stars']){
                if (!this.if_exist(star.name,array) && star.name!==undefined) { 
                    array.push(star.name)
                }
            }
        }

        for (let option of array){
            if (option!==this.filter['star']){
                this.stars_serach.innerHTML+='<option value="'+option+'">'+option+'</option>'
            }
        }
    }

    set_producent(data){
        this.producent_serach.innerHTML='<option selected>Select Producent</option>'
        if (this.filter.hasOwnProperty('producent')){
            this.producent_serach.innerHTML='<option selected>'+this.filter['producent']+'</option>'
        }
        let array=[]
        for (let el of data){
            if (!this.if_exist(el['producent'].name,array) && el['producent'].name!==undefined) { 
                array.push(el['producent'].name)
            }
        }

        for (let option of array){
            if (option!==this.filter['producent']){
                this.producent_serach.innerHTML+='<option value="'+option+'">'+option+'</option>'
            }
        }
        

    }

    set_series(data){
        this.series_serach.innerHTML='<option selected>Select series</option>'
        if (this.filter.hasOwnProperty('series')){
            this.series_serach.innerHTML='<option selected>'+this.filter['series']+'</option>'
        }
        let array=[]
        for (let el of data){
            if (!this.if_exist(el['short_series'].name,array)) { 
                array.push(el['short_series'].name)
            }
        }
        
        for (let option of array){
            if (option!==this.filter['series']){
                this.series_serach.innerHTML+='<option value="'+option+'">'+option+'</option>'
            }
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
        this.div_stars='.stars-search'
        this.div_tag='.tag-search'
    }

    set_form(data){
        this.set_series(data)
        this.set_producent(data)
        this.set_stars(data)
        this.set_tag(data)
    }

    html(){
        let form ='<input type="text" class="form-control" placeholder="First name" aria-label="First name">'
        return form
    }

}

class FilterSeries extends Form{ 

    on_init(){
        this.div='.movies-filter'
        this.div_series='.series-search'
        this.div_producets='.producent-search'
        this.div_stars='.stars-search'
        this.div_tag='.tag-search'
    }

    set_form(data){
        this.set_producent(data)
        this.set_stars(data)
        this.set_tag(data)
    }

    html(){
        let form ='<input type="text" class="form-control" placeholder="First name" aria-label="First name">'
        return form
    }

}
