class LoadID{

    data=data
    content='.content'
    constructor(){
        this.content_slector=document.querySelector(this.content)
        if (this.show_name!=""){
            document.querySelector('title').innerHTML=this.data.show_name
        }else{
            document.querySelector('title').innerHTML=this.data.name
        }
        let names=this.content_slector.querySelectorAll('.name_js')
        for (let name of names){
            if (this.show_name!=""){
                name.innerHTML=this.data.show_name
            }else{
                name.innerHTML=this.data.name
            }
        }
        let movie_avatars=document.querySelectorAll('.avatar_js')
        for (let avatar of movie_avatars){
            avatar.setAttribute('src',this.data.avatar)
        }
        let movie_description=document.querySelector('.description_js')
        if (data.description){
            movie_description.innerHTML=data.description
        }
        this.set_elements()    
    }

    set_tags(){
        let stars=document.querySelector('.tags_js')
        let counter=2
        let next=''
        for (let tag of this.data.tags){
            next=""
            if (counter<=this.data.tags.length){
                next=" , "
            }
            stars.innerHTML+='<spam class="tag">'+tag.name+''+next+'</spam>'
            counter++
        }
    }

    set_tabs(arry,div){
        if (arry.length>0){
            let movis_tab =document.querySelectorAll(div)
            for (let tab of movis_tab){
                tab.style.visibility='visible'
            }
        }
    }

    set_active_tabs(){

        let nav_tab =document.querySelectorAll('.nav_tab')
        for (let tab of nav_tab){
            if (tab.style.visibility =='visible'){
                tab.querySelector('button').classList.add('active')
                break;
            }
        }
        let tab_content =document.querySelectorAll('.tab_content')
        for (let tab of tab_content){
            if (tab.style.visibility =='visible'){
                tab.classList.add('active')
                tab.classList.add('show')
                break;
            }
        }


    }

    get_series(div,array,page){
        const series = new SeriesList(div,array)
        series.return_data(page)
    }

    get_top_stars(array,page){
        const series = new StarsList('.top-stars-otput',array)
        series.return_data(page)
    }

    get_banner(){
        function getExt(filename){
            var ext = filename.split('.').pop();
            if(ext == filename) return "";
            return ext;
        }
        function load_banner(data){
            let ext=getExt(data.baner)
            if (ext==="png" || ext==="jpg"){
                let baner=document.querySelector('.baner_js')
                baner.setAttribute('src',data.baner)
            }else{
                let baner=document.querySelector('.baner')
                baner.style.display="none"
            }
        }
        if (this.data.hasOwnProperty('banner')){
            const baners_count=this.data.banner.length
            if (baners_count==0){
                load_banner(this.data)
            }else{
                var item = this.data.banner[Math.floor(Math.random()*baners_count)];
                let baner=document.querySelector('.baner_js')
                baner.setAttribute('src',item)
            }
        }else{
            load_banner(this.data)
        }
    }

    load_galery(array,corent_page){
        let galery=document.querySelector('.galery')

        if (array.hasOwnProperty(corent_page)){
            let new_array=array[corent_page].Objets
            for (let photo of new_array){
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
        this.set_div()
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

    set_div(){
        this.set_tabs(this.photos,'.galery_tab_js')
        this.set_tabs(this.producent_movies,'.movies_series_tab')
        this.set_tabs(this.series,'.series_tab')
        this.set_tabs(this.stars,'.movies_series_stars_tab')
        this.set_active_tabs()
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
        ObjMovieList.return_data(producet_movies_page)
        producet_movies_page++
    }

    create_table_information(){

        let table=document.querySelector('.table_information')
        table.innerHTML+='<tr>'
        if (this.data.country){
            table.innerHTML+='<td>Country</td><td>'+this.data.country+'</td>'
        }
        if (this.data.country){
            table.innerHTML+='<td>Year</td><td>'+this.data.year+'</td>'
        }
        table.innerHTML+='<td>Series</td><td>'+this.data.series.length+'</td>'
        table.innerHTML+='<td>Movies</td><td>'+this.data.movies.length+'</td>'
        table.innerHTML+='<td>Favourite</td><td>'+this.data.favourite+'</td>'
        if (this.data.views>0){
            table.innerHTML+='<td>Views</td><td>'+this.data.views+'</td>'
        }
        if (this.data.likes>0){
            table.innerHTML+='<td>Likes</td><td>'+this.data.likes+'</td>'
        }
        if (this.data.tags.length>0){
            table.innerHTML+='<td>Tags</td><td class="tags_js"></td>'
        }
        table.innerHTML+='</tr>'
    }
}
let stars_galery_page=0
let stars_movies=0
class Star extends LoadID{
    set_elements(){
        this.set_div()
        this.create_table_information()
        this.set_tags()
        this.paginators()
        this.reset_tabs()

        this.load_galery(this.photos,stars_galery_page)
        stars_galery_page++

        this.load_movies(stars_movies)
        stars_movies++

    }

    set_div(){
        this.set_tabs(this.data.movies,'.movies_tab')
        this.set_tabs(this.data.photos,'.galery_tab')
        this.set_active_tabs()
    }

    load_movies(stars_movies){
        let ObjMovieList = new MovieList('.stars-movies-output',this.starsmovies)
        ObjMovieList.return_data(stars_movies)
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

        const PaginatorStars = new Paginator(this.data.movies,8)
        this.starsmovies=PaginatorStars.genrate_pages()
    }

    create_table_information(){
        function count_age(date_of_birth){            
            var birthdate = new Date(date_of_birth);
            var cur = new Date();
            var diff = cur-birthdate;
            var age = Math.floor(diff/31557600000);
            return age
        }
        let table=document.querySelector('.table_information')
        table.innerHTML+='<tr>'

        if (this.data.nationality){
            table.innerHTML+='<td>Nationality</td><td>'+this.data.nationality+'</td>'
        }

        if (this.data.birth_place){
            table.innerHTML+='<td>Birth place</td><td>'+this.data.birth_place+'</td>'
            table.innerHTML+='<td>Date of birth</td><td>'+this.data.date_of_birth+', <b>age '+count_age(this.data.date_of_birth)+' years old</b></td>'
        }

        if (this.data.ethnicity){
            table.innerHTML+='<td>Ethnicity</td><td>'+this.data.ethnicity+'</td>'
        }

        if (this.data.hair_color){
             table.innerHTML+='<td>Hair color</td><td>'+this.data.hair_color+'</td>'
        }

        if (this.data.height > 0){
            table.innerHTML+='<td>Height</td><td>'+this.data.height+' cm</td>'
        }

        if (this.data.weight > 0){
            table.innerHTML+='<td>Weight</td><td>'+this.data.weight+' kg</td>'
        }

        if (this.data.tags.length){
            table.innerHTML+='<td>Tags</td><td class="tags_js"></td>'
        }

        table.innerHTML+='</tr>'
        if (this.data.tags.length == 0 && !this.data.nationality && !this.data.birth_place && !this.data.ethnicity && !this.data.hair_color && this.data.height == 0 && this.data.weight == 0){
            document.querySelector('.tabel-info-js').style.display='none'
            document.querySelector('.only-photo-js').style.display='block'
        }
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
        this.set_div()
        this.reset_tabs()
        this.get_banner()

        this.load_galery(this.photos,photos_galery_page)
        photos_galery_page++

        this.load_movies(series_movies_page)
        series_movies_page++

        this.get_top_stars(this.stars,series_stars_page)
        series_stars_page++

    }

    set_div(){
        this.set_tabs(this.photos,'.galery_tab_js')
        this.set_tabs(this.series_movies,'.movies_series_tab')
        this.set_tabs(this.stars,'.movies_series_stars_tab')
        this.set_active_tabs()
    }


    load_movies(series_movies_page){
        let ObjMovieList = new MovieList('.series-movies-output',this.series_movies)
        ObjMovieList.return_data(series_movies_page)
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
            table.innerHTML+='<td>Producent</td><td class="producent_item"><a href="'+this.data.producent.dir+'/producent_id.html">'+this.data.producent.name+'</a></td>'
        }
        if (this.data.country){
            table.innerHTML+='<td>Country</td><td>'+this.data.country+'</td>'
        }
        if (this.data.years){
            table.innerHTML+='<td>Years</td><td>'+this.data.years+'</td>'
        }
        table.innerHTML+='<td>Movies</td><td>'+this.data.movies.length+'</td>'
        table.innerHTML+='<td>Number of sezons</td><td>'+this.data.number_of_sezons+'</td>'

        if (this.data.favourite != undefined){
            table.innerHTML+='<td>Favourite</td><td>'+this.data.favourite+'</td>'
        }
        
        if (this.data.views>0){
            table.innerHTML+='<td>Views</td><td>'+this.data.views+'</td>'
        }

        if (this.data.likes>0){
            table.innerHTML+='<td>Views</td><td>'+this.data.likes+'</td>'
        }

        if (this.data.tags.length > 0){
            table.innerHTML+='<td>Tags</td><td class="tags_js"></td>'
        }
        table.innerHTML+='</tr>'
    }
}


let movie_galery_page=0
let movies_with_star=0
let movies_in_series=0
class Movie extends LoadID{
    
    found_star(stars,movies){
        function star_found(count,star){
            for (let star_el in count){
                if (count[star_el]["name"]==star){
                    count[star_el]["count"]=count[star_el]["count"]+1
                    return true
                }
            }  
            return false
        }
        function GetSortOrder(prop) {    
            return function(a, b) {    
                if (a[prop] > b[prop]) {    
                    return 1;    
                } else if (a[prop] < b[prop]) {    
                    return -1;    
                }    
                return 0;    
            }    
        }  
        
        let counter = [ ]
        for (let movie of movies){
            for (let star_movie of movie['short_stars']){
                for (let star of stars){
                    if (star_movie.id == star.id){
                        counter.push(star_movie.name)
                    }
                }
            }

        }
        let count = []
        for (let star of counter){ 
            let star_indx = star_found(count,star) 
            if (!star_indx){
                count.push({"name":star,"count":1})
            }
        }
        count.sort(GetSortOrder("count"));
        console.log(count)
        return count[count.length-1]['name']
    }

    set_buttons(){
        let next_star_div = document.querySelector('#next_star')
        if (this.movies_with_stars_no_paginate.length>1){
            let star_name = this.found_star(this.data.short_stars,this.movies_with_stars_no_paginate)
            let get_star_div = document.querySelector('.get_star')
            get_star_div.innerHTML=star_name

            next_star_div.addEventListener("click", function(){
                let index=get_index(obj,obj.movies_with_stars)
                let movie=obj.data.movies_with_stars[next_video(obj,index,obj.data.movies_with_stars)]
                window.location.href=movie.dir+'/movies_id.html'
            });
            
        }else{
            next_star_div.style.display='none'
        }
        
        let get_series_div = document.querySelector('.get_series')
        get_series_div.innerHTML=this.data.short_series.name
        let next_series_div = document.querySelector('#next_series')
        
        let obj=this
        function get_index(obj,array){
            let index = 0
            for(let movie of array){
                if (obj.data['id'] == movie['id']){
                    return index+1
                }
                index++
            }
        }
        function next_video(obj,index,array){
            if (index == array.length){
                return 0
            }
            return index
        }
        next_series_div.addEventListener("click", function(){
            let index=get_index(obj,obj.movies_no_paginate)
            let movie=obj.movies_no_paginate[next_video(obj,index,obj.movies_no_paginate)]
            window.location.href=movie.dir+'/movies_id.html'
        });
    }
    player(){
        function convert_ends(houer_left){
            if (houer_left<10){
                return '0'+houer_left
            }     
            return houer_left
        }
        function convert_time(time){
            let minuts = Math.floor(time/60)
            let houer  =  Math.floor(minuts/60)
            let houer_left  =  Math.floor(minuts % 60)
            let str_time=houer+":"+convert_ends(houer_left)
            return str_time
        }
        this.set_buttons()
        let play = document.querySelector('#play')
        let mute = document.querySelector('#mute')
        let range = document.querySelector('#range')
        let wideo = document.querySelector('#bgvid')
        let wideoTime = document.querySelector('#wideoTime')
        let wideoDuration = document.querySelector('#wideoDuration')
        let fullScreen = document.querySelector('#fullScreen')
        setTimeout(function(){
            wideoTime.innerHTML=wideo.currentTime
            wideoDuration.innerHTML=convert_time(Math.floor(wideo.duration))
        }, 500);
        
        play.addEventListener("click", function(){
           if (wideo.paused){
                wideo.play() 
                document.querySelector('#playbtm').classList.replace('fa-play','fa-pause')
           }else{
                wideo.pause() 
                document.querySelector('#playbtm').classList.replace('fa-pause','fa-play',)
           }

        });

        mute.addEventListener("click", function(){
            if (wideo.muted){
                wideo.muted=false 
                document.querySelector('#mutebtm').classList.replace('fa-volume-mute','fa-volume-up')
            }else{
                wideo.muted=true 
                document.querySelector('#mutebtm').classList.replace('fa-volume-up','fa-volume-mute')
                
            }
        });

        fullScreen.addEventListener("click", function(){
            wideo.requestFullscreen();
        });

        range.addEventListener("input", function(){
            wideo.currentTime=range.value
            range.max=Math.floor(wideo.duration)
        });
        wideo.addEventListener("timeupdate", function(){
            wideoTime.innerHTML= convert_time(Math.floor(wideo.currentTime))
            range.value = wideo.currentTime
            range.max = Math.floor(wideo.duration)
        })
    }
    set_wideo(){
        let wideo_src=document.querySelector('.wideo_src')
        wideo_src.src=this.data.src
        wideo_src.poster=this.data.poster
    }
    set_poster(){
        let poster=document.querySelector('.if_poster')
        let avatar_show=document.querySelector('.cover_show')
        if (this.data.poster){
            poster.style.visibility='visible'
            poster.style.display='block'
            this.set_wideo()
            this.player()
        }else{
            avatar_show.style.visibility='visible'
            avatar_show.style.display='block'
            let poster=document.querySelector('.cover_js')
            poster.setAttribute('src',this.data.avatar)
        }
        let wideo=document.querySelector('.cover_show')
        let obj=this
        wideo.addEventListener("click", function(){
            poster.style.visibility='visible'
            poster.style.display='block'
            let poster_js=document.querySelector('.cover_js')
            poster_js.style.display='none'
            let wideo = document.querySelector('#bgvid')
            obj.set_wideo()
            obj.player()
            wideo.play()
          
        });
    }
    set_elements(){
        this.paginators()
        this.set_poster()
        this.create_table_information()
        this.set_stars()
        this.set_tags()
        this.set_div()

        this.load_galery(this.photos,movie_galery_page)
        movie_galery_page++

        this.all_movies_with_star(movies_with_star)
        movies_with_star++

        this.add_series_movies(movies_in_series)
        movies_in_series++
    }

    set_div(){
        this.set_tabs(this.photos,'.galery_tab_js')
        this.set_tabs(this.series_movies,'.movies_series_tab')
        this.set_tabs(this.movies_with_stars,'.movies_with_stars_tab')
        this.set_active_tabs()
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

    get_movies_series(){
        let return_movies=[]
        for (let movie of movies){
            if(movie.short_series.id==this.data.short_series.id){
                return_movies.push(movie)
            }
        }
        return return_movies
    }

    get_movies_with_stars(){
        let stars_in_movie=this.data.short_stars
        let return_movies=[]
        for (let movie of movies){
            for (let star of movie.short_stars){
                for (let star_in_movie of stars_in_movie){
                    if (star.id == star_in_movie.id){
                        return_movies.push(movie)
                    }
                }
            }
        }
        return return_movies
    }

    paginators(){
        const PaginatorPhoto  = new Paginator(this.data.photos,20)
        this.photos=PaginatorPhoto.genrate_pages()

        this.movies_with_stars_no_paginate = this.get_movies_with_stars()
        const PaginatorMovies = new Paginator(this.movies_with_stars_no_paginate,20)
        this.movies_with_stars=PaginatorMovies.genrate_pages()

        this.movies_no_paginate = this.get_movies_series()
        const PaginatorMoviesSeries = new Paginator(this.movies_no_paginate,20)
        this.series_movies=PaginatorMoviesSeries.genrate_pages()
    }

    all_movies_with_star(page){
        let ObjMovieList = new MovieList('.all_stars_output',this.movies_with_stars)
        ObjMovieList.return_data(page)
    }
    add_series_movies(page){
        let ObjMovieList = new MovieList('.all-in-series',this.series_movies)
        ObjMovieList.return_data(page)
    }

    create_table_information(){
        let table=document.querySelector('.table_information')
        table.innerHTML+='<tr>'
        table.innerHTML+='<td>Producent</td><td class="producent_item"><a href="'+this.data.producent.dir+'/producent_id.html">'+this.data.producent.show_name+'</a></td>'
        table.innerHTML+='</tr>'
        table.innerHTML+='<tr>'
        table.innerHTML+='<td>Serie</td><td class="series_item"><a href="'+this.data.short_series.dir+'/series_id.html">'+this.data.short_series.name+'</a></td>'
        table.innerHTML+='</tr>'
        table.innerHTML+='<tr>'
        if (this.data.short_stars.length>0){
            table.innerHTML+='<td>Stars</td><td class="stars_strig_js"></td>'
        }
        table.innerHTML+='</tr>'
        table.innerHTML+='<tr>'
        if (this.data.tags.length > 0){
            table.innerHTML+='<td>Tags</td><td class="tags_js"></td>'
        }
        table.innerHTML+='</tr>'
        table.innerHTML+='<tr>'
        if (this.data.country){
            table.innerHTML+='<td>Country</td><td>'+this.data.country+'</td>'
        }
        table.innerHTML+='</tr>'
        table.innerHTML+='<tr>'
        if (this.data.date_relesed != 'None'){
            table.innerHTML+='<td>Date relesed</td><td>'+this.data.date_relesed+'</td>'
        }
        table.innerHTML+='</tr>'
        table.innerHTML+='<tr>'
        if (this.data.views > 0){
            table.innerHTML+='<td>Views</td><td>'+this.data.views+'</td>'
        }
        table.innerHTML+='</tr>'
        table.innerHTML+='<tr>'
        if (this.data.likes > 0){
            table.innerHTML+='<td>Likes</td><td>'+this.data.likes+'</td>'
        }
        table.innerHTML+='</tr>'
        table.innerHTML+='<tr>'
        if (this.data.favourite != undefined){
            table.innerHTML+='<td>Favourite</td><td>'+this.data.favourite+'</td>'
         }
        table.innerHTML+='</tr>'
    }
    set_stars(){
        let stars=document.querySelector('.stars_js')
        let stars_strig_js=document.querySelector('.stars_strig_js')
        let counter=2
        let next=''
        for (let star of data.short_stars){
            next=""
            if (counter<=data.short_stars.length){
                next=" , "
            }

            stars.innerHTML+='<a href="'+star.dir+'/stars_id.html"><img src="'+star.avatar+'" class="img-thumbnail star_src"></a>'
            stars_strig_js.innerHTML+="<spam class='star-string'><a href='"+star.dir+"/stars_id.html'>"+star.name+"</a></spam>"+next+""
            counter++
        }
    }
}

