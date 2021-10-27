class LoadID{

    data=data
    content='.content'
    constructor(){
        this.content_slector=document.querySelector(this.content)
        document.querySelector('title').innerHTML=this.data.name
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

class MovieList{
    constructor(data,div_name,div_output){
        this.data=data
        let series_name=document.querySelector(div_name)
        series_name.innerHTML=data.series[0].name
        this.movies_series=document.querySelector( div_output)
    }

    img(movie){
        return '<img style="width: 13rem; height: 15rem;" src="'+movie.avatar+'" class="card-img-top" alt="...">'
    }

    title(movie){
        return '<h5 class="card-title">'+movie.name+'</h5>'
    }

    body(movie){
        function sort_string(string){
            let limit=150
            let str=''
            if (string.length>limit){
                for (let i = 0; i < limit; i++) {
                    str += string[i];
                  }
                return str+' ...'
            }
            return string
        }
        return '<p class="card-text" style="height: 10rem;">'+sort_string(movie.description)+'</p>'
    }

    action_grup(movie){
        let str=''
        str+='<ul class="list-group list-group-flush">'
        str+='<li class="list-group-item"><a href="'+data.series[0].producent.dir+'/producent_id.html" class="card-link">'+data.series[0].producent.name+'</a></li>'
        str+='<li class="list-group-item"><a href="'+data.series[0].dir+'/series_id.html" class="card-link">'+data.series[0].name+'</a></li>'
        str+='<li class="list-group-item"><a href="'+movie.dir+'/movies_id.html" class="card-link">'+movie.name+'</a></li>'
        str+='</ul>'
        return str
    }
    links(movie){
        let str=''
        str+= '<div class="card-body">'
        for (let star of movie.short_stars){
            str+= '<a href="'+star.dir+'/stars_id.html" class="card-link">'+star.name+'</a>'
        }
        str+= '</div>'
        return str
    }

    return_movies(){
        for (let movie of this.data.series[0].movies){
            let str ='<div class="col">'
            str+='<div class="card cart-item" style="width: 13rem; margin:1rem;">'
            str+=this.img(movie)+'<div class="card-body">'+this.title(movie)+' '+this.body(movie)+'</div>'+this.action_grup(movie)+''+this.links(movie)
            str+='</div>'
            str+='</div>'
            this.movies_series.innerHTML+=str
        }
    }
}

class Movie extends LoadID{
    set_elements(){
        let movie_description=document.querySelector('.movie_description_js')
        movie_description.innerHTML=data.description
        let movie_avatars=document.querySelectorAll('.movie_avatar')
        for (let avatar of movie_avatars){
            avatar.setAttribute('src',this.data.avatar)
        }
        this.load_galery()
        this.create_table_information()
        this.shorcut_menu()
        this.set_stars()
        this.set_tags()
        this.add_series_movies()
    }
    add_series_movies(){
        let ObjMovieList = new MovieList(this.data,'.all-series-name','.all-in-series')
        ObjMovieList.return_movies()
        /*
        let series_name=document.querySelector('.all-series-name')
        series_name.innerHTML=this.data.series[0].name
        let movies_series=document.querySelector('.all-in-series')
        function sort_string(string){
            let limit=150
            let str=''
            if (string.length>limit){
                for (let i = 0; i < limit; i++) {
                    str += string[i];
                  }
                return str+' ...'
            }
            return string
        }
        function title(movie){
            return '<h5 class="card-title">'+movie.name+'</h5>'
        }
        function body(movie){
            return '<p class="card-text" style="height: 10rem;">'+sort_string(movie.description)+'</p>'
        }
        function img(movie){
            return '<img style="width: 13rem; height: 15rem;" src="'+movie.avatar+'" class="card-img-top" alt="...">'
        }
        function action_grup(movie){
            let str=''
            str+='<ul class="list-group list-group-flush">'
            str+='<li class="list-group-item"><a href="'+data.series[0].producent.dir+'/producent_id.html" class="card-link">'+data.series[0].producent.name+'</a></li>'
            str+='<li class="list-group-item"><a href="'+data.series[0].dir+'/series_id.html" class="card-link">'+data.series[0].name+'</a></li>'
            str+='<li class="list-group-item"><a href="'+movie.dir+'/movies_id.html" class="card-link">'+movie.name+'</a></li>'
            str+='</ul>'
            return str
        }
        function links(movie){
            let str=''
            str+= '<div class="card-body">'
            for (let star of movie.short_stars){
                str+= '<a href="'+star.dir+'/stars_id.html" class="card-link">'+star.name+'</a>'
            }
            str+= '</div>'
            return str
        }
        for (let movie of this.data.series[0].movies){
            movies_series.innerHTML+='<div class="col"> <div class="card cart-item" style="width: 13rem; margin:1rem;">'+img(movie)+'<div class="card-body">'+title(movie)+' '+body(movie)+'</div>'+action_grup(movie)+''+links(movie)+'</div></div> '
        }
        */
    }
    load_galery(){
        function getExt(filename){
            var ext = filename.split('.').pop();
            if(ext == filename) return "";
            return ext;
        }
        let galery=document.querySelector('.galery')
        for (let photo of this.data.photos){
            let ext= getExt(photo)

            if (ext==="png" || ext==="jpg"){
             galery.innerHTML+='<div class="col"><a href="'+photo+'"><img class="galery-item" src="'+photo+'"></a></div>'
            }
            
        }
        
    }
    create_table_information(){
        let table=document.querySelector('.table_information')
        table.innerHTML+='<tr>'
        table.innerHTML+='<td>Producent</td><td><a href="'+this.data.series[0].producent.dir+'/producent_id.html">'+this.data.series[0].producent.name+'</a></td>'
        table.innerHTML+='</tr>'
        table.innerHTML+='<tr>'
        table.innerHTML+='<td>Serie</td><td><a href="'+this.data.series[0].dir+'/series_id.html">'+this.data.series[0].name+'</a></td>'
        table.innerHTML+='</tr>'
        table.innerHTML+='<tr>'
        table.innerHTML+='<td>Stars</td><td class="stars_strig_js"></td>'
        table.innerHTML+='</tr>'
        table.innerHTML+='<tr>'
        table.innerHTML+='<td>Tags</td><td class="tags_js"></td>'
        table.innerHTML+='</tr>'
        table.innerHTML+='<tr>'
        table.innerHTML+='<td>Country</td><td>'+this.data.country+'</td>'
        table.innerHTML+='</tr>'
        table.innerHTML+='<tr>'
        table.innerHTML+='<td>Year</td><td>'+this.data.year+'</td>'
        table.innerHTML+='</tr>'
        table.innerHTML+='<tr>'
        table.innerHTML+='<td>Views</td><td>'+this.data.views+'</td>'
        table.innerHTML+='</tr>'
        table.innerHTML+='<tr>'
        table.innerHTML+='<td>Likes</td><td>'+this.data.likes+'</td>'
        table.innerHTML+='</tr>'
        table.innerHTML+='<tr>'
        table.innerHTML+='<td>Favourite</td><td>'+this.data.favourite+'</td>'
        table.innerHTML+='</tr>'
    }
    shorcut_menu(){
        let shorcut_menu=document.querySelectorAll('.shorcut_elment')
        shorcut_menu[0].innerHTML=this.data.series[0].producent.name
        shorcut_menu[0].href=this.data.series[0].producent.dir+'/producent_id.html'
        shorcut_menu[1].innerHTML=this.data.series[0].name
        shorcut_menu[1].href=this.data.series[0].dir+'/series_id.html'
        shorcut_menu[2].innerHTML=this.data.name
        shorcut_menu[2].href=this.data.dir+'/movies_id.html'
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