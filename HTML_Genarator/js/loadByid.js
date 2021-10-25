class LoadID{

    data=data
    content='.content'
    constructor(){
        this.content_slector=document.querySelector(this.content)
        document.querySelector('title').innerHTML=this.data.name
        this.set_elements()    
    }
    set_elements(){}

}
class Star extends LoadID{

    set_elements(){
        this.filter='All'
        let name=this.content_slector.querySelector('.name')
        this.movies=this.content_slector.querySelector('.movies')
        this.select=this.content_slector.querySelector('.filter')
        name.innerHTML=this.data.name
        this.on_select(this)
        this.laod_movies()
        this.set_select()
    }

    on_select(Obj){
        this.select.addEventListener("change", function(){
            Obj.movies.innerHTML=""
            Obj.filter=this.value
            Obj.laod_movies()
        })
    }

    set_select(){
        let series = []

        for (let Movie of this.data['movies']){
            if (series.includes(Movie.short_series.name) == false){
                series.push(Movie.short_series.name)
            }
        }
        for (let serie of series){
            this.select.innerHTML+="<option>"+serie+"</option>"
        }
    }

    laod_movies(){
        for (let Movie of this.data['movies']){
            if (Movie.short_series.name == this.filter || this.filter == "All"){
                this.movies.innerHTML+=this.add_movie(Movie)
            }    
        }
    
    }

    add_movie(Movie){
        return '<div class="el"><a href="'+Movie.dir+'/movies_id.html">'+Movie.short_series.name+' - '+Movie.show_name+'</a><div>'  
    }
}

class Series extends LoadID{

    set_elements(){
        this.filter='All'
        this.movies=this.content_slector.querySelector('.movies')
        this.stars_filter=this.content_slector.querySelector('.stars_filter')
        this.sezon_filter=this.content_slector.querySelector('.sezon_filter')
        this.laod_movies()
        this.set_stars()
        this.set_sezons()
        this.on_select(this)
    }

    on_select(Obj){
        this.stars_filter.addEventListener("change", function(){
            Obj.movies.innerHTML=""
            Obj.filter=this.value
            Obj.laod_movies()
        })
    }

    on_select(Obj){
        this.sezon_filter.addEventListener("change", function(){
            Obj.movies.innerHTML=""
            Obj.filter=this.value
            Obj.laod_movies_sezon()
        })
    }

    set_sezons(){
        let sezons = []
        for (let Movie of this.data['movies']){
            if (sezons.includes(Movie.sezon) == false){
                sezons.push(Movie.sezon)
            }
        }
        for (let sezon of sezons){
            this.sezon_filter.innerHTML+="<option>"+sezon+"</option>"
        }
    }

    set_stars(){
        let stars = []
        for (let Movie of this.data['movies']){
            for (let star of Movie.short_stars){
                if (stars.includes(star.name) == false){
                    stars.push(star.name)
                }
            }
        }
        for (let serie of stars){
            this.stars_filter.innerHTML+="<option>"+serie+"</option>"
        }
    }

    laod_movies(){
        for (let Movie of this.data['movies']){
            for(let star of Movie.short_stars){
                if (star.name==this.filter || this.filter == "All"){
                    this.movies.innerHTML+=this.add_movie(Movie)
                }
            }
          
        }
    }

    laod_movies_sezon(){
        for (let Movie of this.data['movies']){
            if (Movie.sezon == this.filter || this.filter == "All"){
                this.movies.innerHTML+=this.add_movie(Movie)
            }    
        }
    }

    add_movie(Movie){
        return '<div class="el"><a href="'+Movie.dir+'/movies_id.html">'+Movie.show_name+'</a><div>'  
    }
}