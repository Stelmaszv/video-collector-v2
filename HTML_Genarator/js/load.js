let page=0
let counter_stan=false
function json_valider(){
    if (content.innerHTML!=""){
        const json_parse = JSON.parse(content.innerHTML);
        //console.log(json_parse)
        for (let el of json_parse['data']){
            movies_data.push(el)
        }
    }
}
class ContentLoader{
    set_list(){
        var content = document.querySelector('.js_data_content');
        const counter = setInterval(function () {
            for (let item of data){
                var script = document.createElement('script');
                script.onload = function () {
                    content.innerHTML=movies
                    json_valider()
                }
                script.src = item;
                document.head.appendChild(script);
            }

            if (movies_data.length==data_count){
                clearInterval(counter)
                counter_stan=true
            }
        }, 1000);
        /*
        var script = document.createElement('script');
        let movies_data =[]
        var content = document.querySelector('.js_data_content');
        console.log(data)
        script.onload = function () {
            if (content.innerHTML==""){
                content.innerHTML=movies
            }
        };
        setInterval(function () {json_valider()}, 1000);
        script.src = data[0]['src'];
        document.head.appendChild(script);
        */
    }

}
class LoadContet{

    constructor(filter=[]){
        this.set_data()
        this.set_list()
        let div_output=document.querySelector(this.div_output)
        div_output.innerHTML=''
        this.ListOBJ = this.set_obj()
        if (this.filter_is_not_empty(filter)){
            let result=this.ListOBJ.return_data_filter(filter,this.results)
            this.results=result
            this.set_list()
            this.ListOBJ = this.set_obj()
        }
        this.ListOBJ.return_data(page)
        page++
    }



    set_list(){
        const PaginatorMovies = new Paginator(this.results,this.limit)
        this.pagineted_data=PaginatorMovies.genrate_pages()
    }
}

class LoadMovies extends LoadContet{

    set_obj(){
        return new MovieList(this.div_output,this.pagineted_data)
    }

    set_data(data=[]){
        this.results=movies_results
        this.div_output='.movies-output'
        this.data=movies
        this.limit=20
    }

    filter_is_not_empty(filter){
        let name= filter.hasOwnProperty('name')
        let raiting= filter.hasOwnProperty('raiting')
        let series= filter.hasOwnProperty('series')
        let producent= filter.hasOwnProperty('producent')
        let star= filter.hasOwnProperty('star')
        let tag= filter.hasOwnProperty('tag')
        return (name || raiting || series || producent || star || tag)
    }
}


class LoadProducentMovies extends LoadMovies{

    set_data(data=[]){
        this.results=movies_results
        this.div_output='.movies-output'
        this.limit=20
    }
}

class LoadMoviesID extends LoadContet{

    set_obj(){
        return new MovieList(this.div_output,this.pagineted_data)
    }

    set_data(data=[]){
        this.results=movies_results
        this.div_output='.series-movies-output'
        this.limit=20
    }

    filter_is_not_empty(filter){
        let name= filter.hasOwnProperty('name')
        let raiting= filter.hasOwnProperty('raiting')
        let star= filter.hasOwnProperty('star')
        let tag= filter.hasOwnProperty('tag')
        let sezon= filter.hasOwnProperty('sezon')
        return (name || raiting || star || tag || sezon)
    }
}

class LoadMoviesSeriesID extends LoadMoviesID{

    set_data(data=[]){
        this.results=movies_results
        this.div_output='.all-in-series'
        this.limit=20
    }
}



class LoadMoviesSeriesWithStarsID extends LoadMoviesSeriesID{
    set_data(data=[]){
        this.results=movies_results
        this.div_output='.all_stars_output'
        this.limit=20
    }

    filter_is_not_empty(filter){
        let name= filter.hasOwnProperty('name')
        let raiting= filter.hasOwnProperty('raiting')
        let tag= filter.hasOwnProperty('tag')
        let series= filter.hasOwnProperty('series')
        let producent= filter.hasOwnProperty('producent')
        let sezon= filter.hasOwnProperty('sezon')
        return (name || raiting || tag || sezon || series || producent)
    }

}


class LoadSeries extends LoadContet{

    set_obj(){
        return new SeriesList(this.div_output,this.pagineted_data)
    }

    set_data(){
        this.div_output='.series-output'
        this.results=series_result
        this.data=series
        this.limit=5
    }

    filter_is_not_empty(filter){
        let name= filter.hasOwnProperty('name')
        let raiting= filter.hasOwnProperty('raiting')
        let producent= filter.hasOwnProperty('producent')
        let star= filter.hasOwnProperty('star')
        let tag= filter.hasOwnProperty('tag')
        return (name || raiting || producent || star || tag)
    }
}

class LoadSeriesID extends LoadSeries{
    
    set_data(){
        this.div_output='.series-movies-output'
        this.results=series
        this.limit=20
    }
}

class LoadStars extends LoadContet{

    set_obj(){
        return new StarsList(this.div_output,this.pagineted_data)
    }

    set_data(){
        this.div_output='.stars-otput'
        this.results=stars_result
        this.limit=15
    }

    filter_is_not_empty(filter){
        let name= filter.hasOwnProperty('name')
        let raiting= filter.hasOwnProperty('raiting')
        let series= filter.hasOwnProperty('series')
        let hair_color = filter.hasOwnProperty('hair-color')
        let tag= filter.hasOwnProperty('tag')
        let age= filter.hasOwnProperty('age')
        return (name || raiting || hair_color || tag || series || age)
    }
}

class LoadStarsID extends LoadStars{
    set_data(){
        this.div_output='.top-stars-otput'
        this.results=stars_result
        this.data=stars_result
        this.limit=15
    }
}


class LoadProducents extends LoadContet{

    set_obj(){
        return new ProducentsList(this.div_output,this.pagineted_data)
    }

    set_data(){
        this.div_output='.producent-otput'
        this.data=producents
        this.results=producent_result
        this.limit=15
    }

    
    filter_is_not_empty(filter){
        let name= filter.hasOwnProperty('name')
        let raiting= filter.hasOwnProperty('raiting')
        let tag= filter.hasOwnProperty('tag')
        return (name || raiting || tag)
    }
}