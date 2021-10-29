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

    load_galery(array){
        function getExt(filename){
            var ext = filename.split('.').pop();
            if(ext == filename) return "";
            return ext;
        }
        let galery=document.querySelector('.galery')
        galery.innerHTML=''
        for (let photo of array){
            let ext= getExt(photo.photo)
            if (ext==="png" || ext==="jpg"){
             galery.innerHTML+='<div class="col"><a href="'+photo.photo+'" data-caption="'+photo.name+'"><img class="galery-item" src="'+photo.photo+'"></a></div>'
            }  
        }
    }

}
class Star extends LoadID{
    set_elements(){
        this.create_table_information()
        this.set_tags()
        this.load_galery(this.data.photos)
        let ObjMovieList = new MovieList(this.data,'.star_name','.stars-movies-output',this.data.movies,this.data.name)
        ObjMovieList.return_movies()
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

class Series extends LoadID{
    set_elements(){
        this.create_table_information()
        this.set_tags()
        this.get_banner()
        this.load_galery(this.data.photos)
        let ObjMovieList = new MovieList(this.data,'.series_name','.series-movies-output',this.data.movies,this.data.name)
        ObjMovieList.return_movies()
    }

    create_table_information(){
        let table=document.querySelector('.table_information')
        table.innerHTML+='<tr>'
        table.innerHTML+='<td>Producent</td><td><a href="'+this.data.producent.dir+'/producent_id.html">'+this.data.producent.name+'</a></td>'
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

class MovieList{
    constructor(data,div_name,div_output,array,tab_name=''){
        this.array=array
        this.data=data
        let series_name=document.querySelector(div_name)
        if (tab_name){
            series_name.innerHTML=tab_name
        }else{
            series_name.innerHTML=data.series[0].name
        }
        this.movies_series=document.querySelector( div_output)
        this.movies_series.innerHTML=''
    }
    sort_string(string,limit){
        let str=''
        if (string.length>limit){
            for (let i = 0; i < limit; i++) {
                str += string[i];
              }
            return str+' ...'
        }
        return string
    }

    img(movie){
        return '<img src="'+movie.avatar+'" class="card-img-top cover" alt="...">'
    }

    body(movie){
        let str=''
        if (movie.description.length==0){
            str="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        }else{
            str=movie.description
        }

        let string='<b class="card-title">'+movie.name+'</b><br>'+str
        return '<p class="card-text">'+this.sort_string(string,165)+'</p>'
    }

    action_grup(movie){
        let str=''
        let index_round = movie.short_stars[Math.floor(Math.random()* movie.short_stars.length)];
        str+='<ul class="list-group list-group-flush">'
        str+='<li class="list-group-item"><a href="'+movie.short_series.dir+'/series_id.html" class="card-link">'+movie.short_series.name+'</a></li>'
        str+='<li class="list-group-item"><a href="'+movie.dir+'/movies_id.html" class="card-link">'+this.sort_string(movie.name,21)+'</a></li>'
        str+='<li class="list-group-item"><a href="'+index_round.dir+'/movies_id.html" class="card-link">'+index_round.name+'</a></li>'
        str+='</ul>'
        return str
    }
    
    return_movies(){
        for (let movie of this.array){
            let str ='<div class="col">'
            str+='<div class="card cart-item">'
            str+=this.img(movie)+'<div class="card-body">'+this.body(movie)+'</div>'+this.action_grup(movie)
            str+='</div>'
            str+='</div>'
            this.movies_series.innerHTML+=str
        }
    }
}

class Movie extends LoadID{
    set_elements(){
        this.load_galery(this.data.photos)
        this.create_table_information()
        this.shorcut_menu()
        this.set_stars()
        this.set_tags()
        this.add_series_movies()
        this.all_movies_with_star()
    }
    all_movies_with_star(){
        function get_movies_white_star(name){
            let stars=[]
            for (let movie of movies){
                for (let objetc of movie['Objets']){
                    for (let star of objetc.short_stars){
                        if (star.name==name){
                            stars.push(objetc)
                        }
                    }
                }
            }
            return stars
        }
        let ObjMovieList = new MovieList(this.data,'.all-with-star-name','.all_stars_output',get_movies_white_star(this.data.short_stars[0].name),this.data.short_stars[0].name)
        ObjMovieList.return_movies()
    }
    add_series_movies(){
        let ObjMovieList = new MovieList(this.data,'.all-series-name','.all-in-series',this.data.series[0].movies)
        ObjMovieList.return_movies()
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
    set_stars(){
        let stars=document.querySelector('.stars_js')
        let stars_strig_js=document.querySelector('.stars_strig_js')
        for (let star of data.short_stars){
            stars.innerHTML+='<a href="'+star.dir+'/stars_id.html"><img src="'+star.avatar+'" class="img-thumbnail star_src"></a>'
            stars_strig_js.innerHTML+="<spam class='star-string'><a href='"+star.dir+"/stars_id.html'>"+star.name+"</a></spam>, "
        }
    }
}