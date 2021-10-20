
function LoadProduentID(){
    function add_Series(series_json){
        series = '<ul>';
        for (let serie of series_json){
            series += '<li><a href="'+serie.dir+'/index.html">'+serie.name+'</a> </li>'
        }
        series += '</ul>';
        return series
    }
    function add_movies(series_json){
        series = '<ul>';
        for (let serie of series_json){
            series += '<li><a href="'+serie.dir+'/index.html">'+serie.name+'</a> </li>'
        }
        series += '</ul>';
        return series
    }
    setTimeout(function(){ 
        let name = document.querySelector(".name"); 
        name.innerHTML = data.name;
        let series_lists = document.querySelector(".series_lists"); 
        series_lists.innerHTML = add_Series(data.series);
        let movies_lists = document.querySelector(".movies_lists"); 
        movies_lists.innerHTML = add_movies(data.movies);
        let head = document.querySelector("title"); 
        head.innerHTML = data.name; 
    }, 10);
}

function LoadMovieID(){
    setTimeout(function(){ 
        function add_stars(series_json){
            series = '<ul>';
            for (let serie of series_json){
                series += '<li><a href="'+serie.dir+'/index.html">'+serie.name+'</a> </li>'
            }
            series += '</ul>';
            return series
        }
        let head = document.querySelector("title"); 
        head.innerHTML = data.show_name; 
        let name = document.querySelector(".name"); 
        name.innerHTML = data.show_name; 
        let wideo_src = document.querySelector(".wideo_src"); 
        wideo_src.src=data.src
        let stars_lists = document.querySelector(".stars_lists"); 
        stars_lists.innerHTML = add_stars(data.short_stars);
    }, 10);
}

class LoadContet{
    listSelector='.list'
    loadMoreSelector='.load_more'
    array_str=''
    max=0
    limit=1
    index=0
    new_data=[]
    add_new_array=[]
    construct() {}

    add_list(list,on_list){
        this.array_str = '<ul>';
        for (let arr_el of list){
            this.array_str += on_list(arr_el)
        }
        this.array_str += '</ul>';
        return this.array_str
    }

    on_more_button(index){
        this.add_new_array=[]
        this.max=this.max+1
        for (let el_nev_in_data of data){
            if (this.index>this.limit && this.limit<this.max){
                if (data.hasOwnProperty(this.index)){
                    this.add_new_array.push(data[this.index])
                }
            }
            this.index=this.index+1
        }
        this.index=this.max
        for (let el_in_add_new_array of this.add_new_array){
            this.on_load(list,el_in_add_new_array)
        }
    }

    load_more(){
        let list = document.querySelector(this.listSelector);
        this.add_new_array=[]
        this.max=this.max+this.limit
        console.log(this.max)
        for (let el_nev_in_data of data){
            if (this.index>this.limit && this.limit<this.max){
                if (data.hasOwnProperty(this.index)){
                    this.add_new_array.push(data[this.index])
                }
            }
            this.index=this.index+1
        }
        this.index=this.max
        for (let el_in_add_new_array of this.add_new_array){
           this.on_load(list,el_in_add_new_array)
        }
    }

    load(){
        let list = document.querySelector(this.listSelector);
        let load_more = document.querySelector(this.loadMoreSelector);
        list.innerHTML=""
        for (let el_in_data of data){
            if (this.index<this.limit){
                this.new_data.push(data[this.index])
            }
            this.index=this.index+1
        }
        this.index=this.limit
        load_more.index=this.index
        load_more.limit=this.limit
        load_more.max=this.max
    
        for (let el of this.new_data){
            this.on_load(list,el)
        }
    }
    on_load(list,el){}
}

class LoadProducent extends LoadContet{
    on_load(list,el){
        list.innerHTML += '<div>';
        list.innerHTML += '<div><a href="'+el.dir+'/index.html">'+el.name+'</a><div>';
        list.innerHTML += '<div><img width="300" height="150" src="'+el.avatar+'"><div>';
        list.innerHTML += this.add_list(el.series,this.on_series_list)
        list.innerHTML += '</div>';
    }
    on_series_list(arr_el){
        return '<li><a href="'+arr_el.dir+'/index.html">'+arr_el.name+'</a> </li>'
    }
}

class LoadMovies extends LoadContet{
    limit=11
    on_load(list,el){
        list.innerHTML += '<div><a href="'+el.dir+'/index.html">'+el.short_series.name+'-'+el.name+'</a><div>';
    }
}

class LoadStars extends LoadContet{
    limit=11
    on_load(list,el){
        list.innerHTML += '<div><a href="'+el.dir+'/index.html">'+el.show_name+'</a><div>';
    }
}
const LoadStarsOBJ=new LoadStars()
const LoadMoviesOBJ=new LoadMovies()
const LoadProducentOBJ=new LoadProducent()