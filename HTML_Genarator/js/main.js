function LoadProduent(){
    function add_Series(series_json){
        series = '<ul>';
        for (let serie of series_json){
            series += '<li><a href="'+serie.dir+'/index.html">'+serie.name+'</a> </li>'
        }
        series += '</ul>';
        return series
    }
    let list = document.querySelector(".list");
    for (let el of data){
        list.innerHTML += '<div>';
        list.innerHTML += '<div><a href="'+el.dir+'/index.html">'+el.name+'</a><div>';
        list.innerHTML += '<div><img width="300" height="150" src="'+el.avatar+'"><div>';
        list.innerHTML += add_Series(el.series)
        list.innerHTML += '</div>';
    }
};

function LoadProduentID(){
    function add_Series(series_json){
        series = '<ul>';
        for (let serie of series_json){
            series += '<li><a href="'+serie.dir+'/series_id.html">'+serie.name+'</a> </li>'
        }
        series += '</ul>';
        return series
    }
    function add_movies(series_json){
        series = '<ul>';
        for (let serie of series_json){
            series += '<li><a href="'+serie.dir+'/movies_id.html">'+serie.name+'</a> </li>'
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
                series += '<li><a href="'+serie.dir+'/stars_id.html">'+serie.name+'</a> </li>'
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
    on_load(list,el){}
}

class LoadMovies extends LoadContet{
    limit=5
    on_load(list,el){
        list.innerHTML += '<div class="el"><a href="'+el.dir+'/movies_id.html">'+el.short_series.name+'-'+el.name+'</a><div>';
    }
}

class LoadStars extends LoadContet{
    limit=10
    on_load(list,el){
        list.innerHTML += '<div class="el"><a href="'+el.dir+'/stars_id.html">'+el.show_name+'</a><div>';
    }
}

class LoadProducent extends LoadContet{
    limit=20
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
max=0
add_new_array=[]
index=0
function LoadMore(OBJ){
    console.log(index)
    var show=0
    var limit=OBJ.limit
    if (max!=0){
        show=show+OBJ.limit
    }
    max=max+OBJ.limit
    let list = document.querySelector(OBJ.listSelector);
    for (let el_nev_in_data of data){
        if (index=>show && index<limit){
            add_new_array.push(el_nev_in_data)
            show=show+1
        }
        index=index+1
    }

    for (let el_in_add_new_array of add_new_array){
        OBJ.on_load(list,el_in_add_new_array)
    }
}