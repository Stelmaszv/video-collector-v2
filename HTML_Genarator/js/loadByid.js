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
        let movie_avatars=document.querySelectorAll('.avatar_js')
        for (let avatar of movie_avatars){
            avatar.setAttribute('src',this.data.avatar)
        }
        let movie_description=document.querySelector('.description_js')
        movie_description.innerHTML=data.description
        this.set_elements()    
    }

    set_tags(){
        let stars=document.querySelector('.tags_js')
        for (let tag of this.data.tags){
            stars.innerHTML+='<spam class="tag">'+tag.name+'</spam>'
        }
    }

    get_series(div,array,page){
        const series = new SeriesList(div,array)
        series.return_series(page)
    }

    get_top_stars(array,page){
        const series = new StarsList('.top-stars-otput',array)
        series.return_stars(page)
    }

    get_banner(){
        function getExt(filename){
            var ext = filename.split('.').pop();
            if(ext == filename) return "";
            return ext;
        }
        let ext=getExt(this.data.baner)
        if (ext==="png" || ext==="jpg"){
            let baner=document.querySelector('.baner_js')
            baner.setAttribute('src',this.data.baner)
        }else{
            let baner=document.querySelector('.baner')
            baner.style.display="none"
        }
    }

    load_galery(array,corent_page){
        function getExt(filename){
            var ext = filename.split('.').pop();
            if(ext == filename) return "";
            return ext;
        }
        let galery=document.querySelector('.galery')

        if (array.hasOwnProperty(corent_page)){
            let new_array=array[corent_page].Objets
            for (let photo of new_array){
                let ext= getExt(photo.photo)
                if (ext==="png" || ext==="jpg")
                galery.innerHTML+='<div class="col"><a href="'+photo.photo+'" data-caption="'+photo.name+'"><img class="galery-item" src="'+photo.photo+'"></a></div>'
            }
        }  
    }
}

let producet_galery_page=0
let producet_movies_page=0
let producet_series_page=0
let producet_stars_page=0
class Producnet extends LoadID{
    series_output_div='.series-movies-output' 
    set_elements(){
        this.create_table_information()
        this.set_tags()
        this.get_banner()
        this.paginators()
        this.reset_tabs()

        this.get_top_stars(this.stars,producet_stars_page)
        producet_stars_page++

        this.get_series('.series-movies-output',this.series,producet_series_page)
        producet_series_page++

        this.load_movies(producet_movies_page)
        producet_movies_page++
 
        this.load_galery(this.photos,producet_galery_page)
        producet_galery_page++
    }

    reset_tabs(){
        let series=document.querySelector('.series-movies-output')
        let galery=document.querySelector('.galery')
        let movies_output=document.querySelector('.movies-output')
        let top_stars=document.querySelector('.top-stars-otput')
        movies_output.innerHTML=''
        galery.innerHTML=''
        series.innerHTML=''
        top_stars.innerHTML=''
    }

    paginators(){
        const PaginatorMovies = new Paginator(this.data.movies,20)
        const PaginatorPhoto  = new Paginator(this.data.photos,20)
        const PaginatorStars  = new Paginator(this.data.stars,4)
        const PaginatorSeries = new Paginator(this.data.series,5)
        this.stars=PaginatorStars.genrate_pages()
        this.series=PaginatorSeries.genrate_pages()
        this.photos=PaginatorPhoto.genrate_pages()
        this.producent_movies=PaginatorMovies.genrate_pages()
    }

    load_movies(producet_movies_page){
        let ObjMovieList = new MovieList('.movies-output',this.producent_movies)
        ObjMovieList.return_movies(producet_movies_page)
        producet_movies_page++
    }

    create_table_information(){

        let table=document.querySelector('.table_information')
        table.innerHTML+='<tr>'
        table.innerHTML+='<td>Country</td><td>'+this.data.country+'</td>'
        table.innerHTML+='<td>Year</td><td>'+this.data.year+'</td>'
        table.innerHTML+='<td>Favourite</td><td>'+this.data.favourite+'</td>'
        table.innerHTML+='<td>Views</td><td>'+this.data.views+'</td>'
        table.innerHTML+='<td>Likes</td><td>'+this.data.likes+'</td>'
        table.innerHTML+='<td>Tags</td><td class="tags_js"></td>'
        table.innerHTML+='</tr>'
    }
}
let stars_galery_page=0
let stars_movies=0
class Star extends LoadID{
    set_elements(){
        this.create_table_information()
        this.set_tags()
        this.paginators()
        this.reset_tabs()

        this.load_galery(this.photos,stars_galery_page)
        stars_galery_page++

        this.load_movies(stars_movies)
        stars_movies++

    }

    load_movies(stars_movies){
        let ObjMovieList = new MovieList('.stars-movies-output',this.starsmovies)
        ObjMovieList.return_movies(stars_movies)
    }

    reset_tabs(){
        let galery=document.querySelector('.galery')
        galery.innerHTML=''

        let star_movies_output=document.querySelector('.stars-movies-output')
        star_movies_output.innerHTML=''
    }

    paginators(){
        const PaginatorPhoto = new Paginator(this.data.photos,10)
        this.photos=PaginatorPhoto.genrate_pages()

        const PaginatorStars = new Paginator(this.data.movies,1)
        this.starsmovies=PaginatorStars.genrate_pages()
    }

    create_table_information(){
        function count_age(){
            return '25'
        }
        let table=document.querySelector('.table_information')
        table.innerHTML+='<tr>'
        table.innerHTML+='<td>Nationality</td><td>'+this.data.nationality+'</td>'
        table.innerHTML+='<td>Birth place</td><td>'+this.data.birth_place+'</td>'
        table.innerHTML+='<td>Date of birth</td><td>'+this.data.date_of_birth+', <b>age '+count_age(this.data.date_of_birth)+' years old</b></td>'
        table.innerHTML+='<td>Ethnicity</td><td>'+this.data.ethnicity+'</td>'
        table.innerHTML+='<td>Hair color</td><td>'+this.data.hair_color+'</td>'
        table.innerHTML+='<td>Height</td><td>'+this.data.height+' cm</td>'
        table.innerHTML+='<td>Weight</td><td>'+this.data.weight+' kg</td>'
        table.innerHTML+='<td>Tags</td><td class="tags_js"></td>'
        table.innerHTML+='</tr>'
    }
}
let photos_galery_page=0
let series_movies_page=0
let series_stars_page=0
class Series extends LoadID{
    set_elements(){
        this.create_table_information()
        this.set_tags()

        this.paginators()
        this.reset_tabs()
        this.get_banner()

        this.load_galery(this.photos,photos_galery_page)
        photos_galery_page++

        this.load_movies(series_movies_page)
        series_movies_page++

        this.get_top_stars(this.stars,series_stars_page)
        series_stars_page++

    }

    load_movies(series_movies_page){
        let ObjMovieList = new MovieList('.series-movies-output',this.series_movies)
        ObjMovieList.return_movies(series_movies_page)
    }

    reset_tabs(){

        let galery=document.querySelector('.galery')
        galery.innerHTML=''

        let series=document.querySelector('.series-movies-output')
        series.innerHTML=''

        let top_stars=document.querySelector('.top-stars-otput')
        top_stars.innerHTML=''

    }

    paginators(){
        const PaginatorPhoto  = new Paginator(this.data.photos,10)
        this.photos=PaginatorPhoto.genrate_pages()

        const PaginatorMovies = new Paginator(this.data.movies,20)
        this.series_movies=PaginatorMovies.genrate_pages()

        const PaginatorStars  = new Paginator(this.data.stars,4)
        this.stars=PaginatorStars.genrate_pages()

    }

    create_table_information(){
        let table=document.querySelector('.table_information')
        table.innerHTML+='<tr>'
        if (this.data.producent.hasOwnProperty('dir')){
            table.innerHTML+='<td>Producent</td><td><a href="'+this.data.producent.dir+'/producent_id.html">'+this.data.producent.name+'</a></td>'
        }
        table.innerHTML+='<td>Country</td><td>'+this.data.country+'</td>'
        table.innerHTML+='<td>Years</td><td>'+this.data.years+'</td>'
        table.innerHTML+='<td>Number of sezons</td><td>'+this.data.number_of_sezons+'</td>'
        table.innerHTML+='<td>Favourite</td><td>'+this.data.favourite+'</td>'
        table.innerHTML+='<td>Views</td><td>'+this.data.views+'</td>'
        table.innerHTML+='<td>Likes</td><td>'+this.data.likes+'</td>'
        table.innerHTML+='<td>Tags</td><td class="tags_js"></td>'
        table.innerHTML+='</tr>'
    }
}


let movie_galery_page=0
let movies_with_star=0
let movies_in_series=0
class Movie extends LoadID{
    set_elements(){
        this.create_table_information()
        this.set_stars()
        this.set_tags()
        this.paginators()

        this.load_galery(this.photos,movie_galery_page)
        movie_galery_page++

        this.all_movies_with_star(movies_with_star)
        movies_with_star++

        this.add_series_movies(movies_in_series)
        movies_in_series++
    }

    reset_tabs(){
        let series=document.querySelector('.series-movies-output')
        let galery=document.querySelector('.galery')
        let movies_output=document.querySelector('.movies-output')
        let top_stars=document.querySelector('.top-stars-otput')
        movies_output.innerHTML=''
        galery.innerHTML=''
        series.innerHTML=''
        top_stars.innerHTML=''
    }

    paginators(){
        const PaginatorPhoto  = new Paginator(this.data.photos,10)
        this.photos=PaginatorPhoto.genrate_pages()

        const PaginatorMovies = new Paginator(this.data.movies_with_stars,1)
        this.movies=PaginatorMovies.genrate_pages()

        const PaginatorMoviesSeries = new Paginator(this.data.series[0].movies,5)
        this.series_movies=PaginatorMoviesSeries.genrate_pages()
    }

    all_movies_with_star(page){
        let ObjMovieList = new MovieList('.all_stars_output',this.movies)
        ObjMovieList.return_movies(page)
    }
    add_series_movies(page){
        let ObjMovieList = new MovieList('.all-in-series',this.series_movies)
        ObjMovieList.return_movies(page)
    }

    create_table_information(){
        let table=document.querySelector('.table_information')
        table.innerHTML+='<tr>'
        if (this.data.series[0].producent.hasOwnProperty('dir')){
            table.innerHTML+='<td>Producent</td><td><a href="'+this.data.series[0].producent.dir+'/producent_id.html">'+this.data.series[0].producent.name+'</a></td>'
        }
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
    set_stars(){
        let stars=document.querySelector('.stars_js')
        let stars_strig_js=document.querySelector('.stars_strig_js')
        for (let star of data.short_stars){
            stars.innerHTML+='<a href="'+star.dir+'/stars_id.html"><img src="'+star.avatar+'" class="img-thumbnail star_src"></a>'
            stars_strig_js.innerHTML+="<spam class='star-string'><a href='"+star.dir+"/stars_id.html'>"+star.name+"</a></spam>, "
        }
    }
}

