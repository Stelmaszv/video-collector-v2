let scroller = function(){
    window.addEventListener("scroll", (event) => {
        var limit = document.body.offsetHeight - window.innerHeight;
        let scrol_pos=90/100*limit
        if (window.scrollY>scrol_pos){
            LoadMoviesObjInit.ListOBJ.return_data(page++)
        }
    });
}

let keyup = function(form,methods,object,defult){
    let search = ''
    if (!defult){
        search =document.querySelector('.name-search')
    }else{
        search =document.querySelector(defult)
    }
    search.addEventListener("keyup", function(){
        if (this.value.length>2){
            page=0
            filter["name"] = this.value
            LoadMoviesObjInit = new object(filter)
            LoadMoviesObjInit.div_output.innerHTML=''

            for (let method of methods){

                if (method=='set_producent'){
                    form.set_producent(LoadMoviesObjInit.results)
                }
    
                if (method=='set_stars'){
                    form.set_stars(LoadMoviesObjInit.results)
                }
    
                if (method=='set_tag'){
                    form.set_tag(LoadMoviesObjInit.results)
                }
    
                if (method == 'set_series'){
                    form.set_series(LoadMoviesObjInit.results)
                }
            }

        }

    });
}

let change = function (selector,key,form,methods,object){
    let search_raiting =document.querySelector(selector)
    search_raiting.addEventListener("change", function(){
        page=0
        filter[key] = this.value
        LoadMoviesObjInit = new object(filter)
        LoadMoviesObjInit.div_output.innerHTML=''

        for (let method of methods){

            if (method=='set_producent'){
                form.set_producent(LoadMoviesObjInit.results)
            }

            if (method=='set_stars'){
                form.set_stars(LoadMoviesObjInit.results)
            }

            if (method=='set_tag'){
                form.set_tag(LoadMoviesObjInit.results)
            }

            if (method == 'set_series'){
                form.set_series(LoadMoviesObjInit.results)
            }

            if (method == 'set_hair_color'){
                form.set_hair_color(LoadMoviesObjInit.results)
            }

        }

    });
}



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


class FilterMoviesID extends Form{ 

    on_init(){
        this.div='.movies-filter'
        this.div_series='.series-search'
        this.div_producets='.producent-search'
        this.div_stars='.stars-search'
        this.div_tag='.tag-search'
        this.div_sezon='.season-search'
    }

    set_form(data){
        this.set_sezons(data)
        this.set_stars(data)
        this.set_tag(data)
    }

    set_sezons(data){
        this.div_sezon_html=document.querySelector(this.div_sezon)
        this.div_sezon_html.innerHTML='<option selected>Select series</option>'
        if (this.filter.hasOwnProperty('sezon')){
            this.div_sezon_html.innerHTML='<option selected>'+this.filter['sezon']+'</option>'
        }
        let array=[]
        for (let el of data){
            if (!this.if_exist(el.sezon*1,array)) { 
                array.push(el.sezon*1)
            }
        }
        array.sort(function(a, b){return a-b})
        for (let option of array){
            let end_option = ''
            if (option!==this.filter['sezon']){
                if (option<10){
                    end_option=option
                }else{
                    end_option=option
                }
                this.div_sezon_html.innerHTML+='<option value="'+option+'">'+end_option+'</option>'
            }
        }
    }

    html(){
        let form ='<input type="text" class="form-control" placeholder="First name" aria-label="First name">'
        return form
    }

}

class FilterStars extends Form{ 

    on_init(){
        this.div='.movies-filter'
        this.div_series='.series-search'
        this.div_producets='.producent-search'
        this.div_stars='.stars-search'
        this.div_tag='.tag-search'
        this.hair_color_div=".hair-color-search"
    }

    set_form(data){
        this.set_tag(data)
        this.set_series(data)
        this.set_hair_color(data)
    }

    set_hair_color(data){
        this.hair_color_search = document.querySelector(this.hair_color_div)
        this.hair_color_search.innerHTML='<option selected>Select series</option>'
        if (this.filter.hasOwnProperty('hair_color')){
            this.hair_color_search.innerHTML='<option selected>'+this.filter['hair_color']+'</option>'
        }
        let array=[]
        for (let el of data){
            if (!this.if_exist(el.hair_color,array)) { 
                array.push(el.hair_color)
            }
        }
        
        for (let option of array){
            if (option!==this.filter['hair_color'] && option!=''){
                this.hair_color_search.innerHTML+='<option value="'+option+'">'+option+'</option>'
            }
        }
    }

    html(){
        let form ='<input type="text" class="form-control" placeholder="First name" aria-label="First name">'
        return form
    }

}
class FilterStarsID extends FilterStars{ 

    set_form(data){
        this.set_hair_color(data)
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
        this.set_tag(data)
        this.set_producent(data)
        this.set_stars(data)
    }
}

class FilterProducent extends Form{ 

    on_init(){
        this.div='.movies-filter'
        this.div_series='.series-search'
        this.div_producets='.producent-search'
        this.div_stars='.stars-search'
        this.div_tag='.tag-search'
    }

    set_form(data){
        this.set_tag(data)
    }

}

