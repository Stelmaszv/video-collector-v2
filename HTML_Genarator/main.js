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

function LoadMovies(){
    max=0
    let list = document.querySelector(".list");
    let load_more = document.querySelector(".load_more");
    load_more.addEventListener("click", function(){
        add_new_array=[]
        max=max+data_limit
        for (let el_nev_in_data of data){
            if (index>data_limit && index<max){
                if (data.hasOwnProperty(index)){
                add_new_array.push(data[index])
                }
            }
            index=index+1
        }
        index=max
        for (let el_in_add_new_array of add_new_array){
            list.innerHTML += '<div><a href="'+el_in_add_new_array.dir+'/index.html">'+el_in_add_new_array.short_series.name+'-'+el_in_add_new_array.name+'</a><div>';
        }
    });
    list.innerHTML=""
    data_limit=51
    new_data=[]
    index=0
    for (let el_in_data of data){
        if (index<data_limit){
            new_data.push(data[index])
        }
        index=index+1
    }
    index=data_limit
    for (let el_in_nev_data of new_data){
        list.innerHTML += '<div><a href="'+el_in_nev_data.dir+'/index.html">'+el_in_nev_data.short_series.name+'-'+el_in_nev_data.name+'</a><div>';
    }

}