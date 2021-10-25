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
        this.movies=this.content_slector.querySelector('.movies')
        this.laod_movies()
        this.set_stars()
    }

    set_stars_stars(){
        let stars = []
        for (let Movie of this.data['movies']){
            if (series.includes(Movie.stars) == false){
                stars.push(Movie.short_series.name)
            }
        }
    }

    laod_movies(){
        for (let Movie of this.data['movies']){
            this.movies.innerHTML+=this.add_movie(Movie) 
        }
    }

    add_movie(Movie){
        return '<div class="el"><a href="'+Movie.dir+'/movies_id.html">'+Movie.show_name+'</a><div>'  
    }
}