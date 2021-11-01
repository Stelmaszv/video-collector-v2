let page=0
class LoadContet{}

class LoadMovies{

    limit=20

    constructor(){
        this.set_list(this.limit)

        let movies_div=document.querySelector('.movies-output')
        movies_div.innerHTML=''

        this.load_movies(page)
        page++

    }
    
    set_list(limit){
        const PaginatorMovies = new Paginator(movies,limit)
        this.movies=PaginatorMovies.genrate_pages()
    
    }

    load_movies(page){
        let ObjMovieList = new MovieList('.movies-output',this.movies)
        ObjMovieList.return_movies(page)
    }
}
/*
class LoadContet{
    listSelector='.list'
    loadMoreSelector='.load_more'
    end=false

    construct(){
        this.load_more(this)
    }

    add_list(list,on_list){
        this.array_str = '<ul>';
        for (let arr_el of list){
            this.array_str += on_list(arr_el)
        }
        this.array_str += '</ul>';
        return this.array_str
    }

    load_more(OBJ){
        let list = document.querySelector(OBJ.listSelector);
        let load_more=document.querySelector(OBJ.loadMoreSelector);
        load_more.addEventListener("click", function(){
            if (OBJ.end == false){
                if (OBJ.data.hasOwnProperty(page)){
                    for (let el_in_nev_data of OBJ.data[page]['Objets']){
                        OBJ.on_load(list,el_in_nev_data)
                    }
                    if (OBJ.data.hasOwnProperty(page+1)){
                        page=page+1
                    }else{
                        OBJ.end=true
                        load_more.innerHTML=''
                    }

                }
            }
        });
    }
}

class LoadMovies extends LoadContet{
    data=movies
    on_load(list,el){
        list.innerHTML += '<div class="el"><a href="'+el.dir+'/movies_id.html">'+el.short_series[0].name+'-'+el.name+'</a><div>';
    }
}

class LoadStars extends LoadContet{
    data=stars
    on_load(list,el){
        list.innerHTML += '<div class="el"><a href="'+el.dir+'/stars_id.html">'+el.show_name+'</a><div>';
    }
}

class LoadProducent extends LoadContet{
    data=producents
    on_load(list,el){
        list.innerHTML += '<div class="el">';
        list.innerHTML += '<div><a href="'+el.dir+'/producent_id.html">'+el.name+'</a><div>';
        list.innerHTML += '<div><img width="300" height="150" src="'+el.avatar+'"><div>';
        list.innerHTML += this.add_list(el.series,this.on_series_list)
        list.innerHTML += '</div>';
    }
    on_series_list(arr_el){
        return '<li class="el"><a href="'+arr_el.dir+'/series_id.html">'+arr_el.name+'</a> </li>'
    }
}

class LoadSeries extends LoadContet{
    data=series
    on_load(list,el){
        list.innerHTML += '<div class="el"><a href="'+el.dir+'/stars_id.html">'+el.show_name+'</a><div>';
    }
}

*/