let page=0
class LoadContet{}

class LoadMovies{

    limit=20

    constructor(){
        this.set_list(this.limit)

        let movies_div=document.querySelector('.movies-output')
        movies_div.innerHTML=''

        this.load(page)
        page++

    }
    
    set_list(limit){
        const PaginatorMovies = new Paginator(movies,limit)
        this.movies=PaginatorMovies.genrate_pages()
    
    }

    load(page){
        let ObjMovieList = new MovieList('.movies-output',this.movies)
        ObjMovieList.return_movies(page)
    }
}

class LoadSeries{

    limit=5

    constructor(){
        this.set_list(this.limit)

        let series_div=document.querySelector('.series-output')
        series_div.innerHTML=''

        this.load(page)
        page++
    }

    set_list(limit){
        const PaginatorMovies = new Paginator(series,limit)
        this.series=PaginatorMovies.genrate_pages()
    }

    load(page){
        const series = new SeriesList('.series-output',this.series)
        series.return_series(page)
    }
}

class LoadStars{

    limit=15

    constructor(){
        this.set_list(this.limit)

        let stars_otput=document.querySelector('.stars-otput')
        stars_otput.innerHTML=''

        this.load(page)
        page++
    }


    set_list(limit){
        const PaginatorStars = new Paginator(stars,limit)
        this.stars=PaginatorStars.genrate_pages()
    }

    load(page){
        const series = new StarsList('.stars-otput',this.stars)
        series.return_stars(page)
    }
}


class LoadProducents{

    limit=10

    constructor(){
        this.set_list(this.limit)

        let producent_otput=document.querySelector('.producent-otput')
        producent_otput.innerHTML=''

        this.load(page)
        page++
    }


    set_list(limit){
        const PaginatorStars = new Paginator(producents,limit)
        this.producents=PaginatorStars.genrate_pages()
    }

    load(page){
        const producents = new ProducentsList('.producent-otput',this.producents)
        producents.return_pages(page)
    }
}