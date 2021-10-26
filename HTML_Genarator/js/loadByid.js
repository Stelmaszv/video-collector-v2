class LoadID{

    data=data
    content='.content'
    constructor(){
        this.content_slector=document.querySelector(this.content)
        let names=this.content_slector.querySelectorAll('.name_js')
        for (let name of names){
            name.innerHTML=this.data.name
        }
        this.set_elements()    
    }
    set_elements(){}

}
class Star extends LoadID{

    set_elements(){
        this.filter='All'
        this.movies=this.content_slector.querySelector('.movies')
        this.select=this.content_slector.querySelector('.filter')
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

class Movie extends LoadID{
    set_elements(){
        let producent=document.querySelector('.producent-js')
        producent.innerHTML='Producent'
        let series=document.querySelectorAll('.series-js')
        for (let serie of series){
            serie.innerHTML=data.short_series.name
        }
        let movie=document.querySelector('.movie-js')
        movie.innerHTML=data.name
        let movie_avatars=document.querySelectorAll('.movie_avatar')
        for (let avatar of movie_avatars){
            avatar.setAttribute('src',this.data.avatar)
        }
        let movie_description=document.querySelector('.movie_description_js')
        movie_description.innerHTML=data.description
        this.set_stars()
        this.set_tags()
    }
    set_tags(){
        let stars=document.querySelector('.tags_js')
        for (let tag of this.data.tags){
            stars.innerHTML+='<spam class="tag">'+tag.name+'</spam>'
        }
    }
    set_stars(){
        let stars=document.querySelector('.stars_js')
        let stars_strig_js=document.querySelector('.stars_strig_js')
        for (let star of data.short_stars){
            stars.innerHTML+='<a href="'+star.dir+'/stars_id.html"><img src="'+star.avatar+'" class="img-thumbnail star_src"></a>'
            stars_strig_js.innerHTML+="<spam class='star-string'><a href='"+star.dir+"/stars_id.html'>"+star.name+"</a></spam>"
        }
    }
}