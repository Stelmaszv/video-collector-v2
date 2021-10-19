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
        movies_lists.innerHTML = add_movies(data.series);
        let head = document.querySelector("title"); 
        head.innerHTML = data.name; 
    }, 10);

    

}