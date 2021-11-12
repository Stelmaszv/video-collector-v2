class List{

    constructor(div_output,array){
        this.array=array
        this.div_output=document.querySelector(div_output)
    }

    return_data_filter(filter,array){

        if(filter.hasOwnProperty('hair-color')){
            let value   = filter['hair-color']
            let result  =[]

            for (let data of array) {
                if (data['hair_color'] == value){
                    result.push(data)
                }
            }
            return result
        }

        if (filter.hasOwnProperty('raiting')){
            let raiting   = filter['raiting']
            let result=[]

            for (let data of array) {
                if (data.rating==raiting){
                    result.push(data)
                }
            }
            return result
        }

        if (filter.hasOwnProperty('sezon')){
            let value   = filter['sezon']
            let result=[]

            for (let data of array) {
                if (data.sezon==value){
                    result.push(data)
                }
            }
            return result
        }

        if(filter.hasOwnProperty('age')){
            function count_age(date_of_birth){            
                var birthdate = new Date(date_of_birth);
                var cur = new Date();
                var diff = cur-birthdate;
                var age = Math.floor(diff/31557600000);
                return age
            }
            let value   = filter['age']
            let result  =[]
            for (let data of array) {
                if (data.date_of_birth!="None"){
                    if (count_age(data.date_of_birth)<=value){
                        result.push(data)
                    }
                }
            }
            return result
        }

        if(filter.hasOwnProperty('series')){
            let value   = filter['series']
            let result=[]
            for (let data of array) {
                if (data['short_series'].name == value){
                    result.push(data)
                }
            }
            return result
        }

        if(filter.hasOwnProperty('name')){
            let value   = filter['name']
            let result=[]
            for (let data of array) {
                let re = new RegExp(value);
                let req_exp = re.test(data.name);
                if (req_exp){
                    result.push(data)
                }
            }
            return result
        }

        if(filter.hasOwnProperty('producent')){
            let value   = filter['producent']
            let result=[]
            for (let data of array) {
                if (data['producent'].name == value){
                    result.push(data)
                }
            }
            return result
        }

        if (filter.hasOwnProperty('tag')){
            let value   = filter['tag']
            let result=[]
            for (let data of array) {
                for (let tag of data['tags']){
                    if (tag.name == value){
                        result.push(data)
                    }
                }
            }
            return result
        } 

        if(filter.hasOwnProperty('star')){
            let value   = filter['star']
            let result=[]
            for (let data of array) {
                for (let star of data['short_stars']){
                    if (star.name == value){
                        result.push(data)
                    }
                }
            }
            return result
        }
    }
}

class MovieList extends List{

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
        return '<a href="'+movie.dir+'/movies_id.html"><img src="'+movie.avatar+'" class="card-img-top cover"></a>'
    }

    show_movie_name(movie){
        if (movie.show_name!=""){
            return movie.show_name
        }
        return movie.name
    }

    body(movie){
        let str=''
        if (movie.description.length==0){
            str="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        }else{
            str=movie.description
        }
        let name='<a href="'+movie.dir+'/movies_id.html" >'+this.show_movie_name(movie)+'</a>'
        let string=name+'<br>'+str
        return '<p class="card-text">'+this.sort_string(string,220)+'</p>'
    }

    action_grup(movie){
        let str=''
        let more=''
        let index_round=movie.short_stars[0]
        if (movie.short_stars.length>1){
            index_round = movie.short_stars[Math.floor(Math.random()* movie.short_stars.length)];
            let number = movie.short_stars.length-1
            more='<i> + '+number+'</i>'
        }
        str+='<ul class="list-group list-group-flush">'
        str+='<li class="list-group-item"><a href="'+movie.short_series.dir+'/series_id.html" class="card-link">'+movie.short_series.name+'</a></li>'
        if (movie.short_stars.length>0){
            str+='<li class="list-group-item"><a href="'+index_round.dir+'/stars_id.html" class="card-link">'+index_round.name+'</a>'+more+'</li>'
        }
        str+='</ul>'
        return str
    }
    
    return_data(page){
        if (this.array.hasOwnProperty(page)){
            let array=this.array[page].Objets
            for (let movie of array){
                let str ='<div class="col">'
                str+='<div class="card cart-item">'
                str+=this.img(movie)+'<div class="card-body">'+this.body(movie)+'</div>'+this.action_grup(movie)
                str+='</div>'
                str+='</div>'
                this.div_output.innerHTML+=str
            }
        }

    }
}
class SeriesList extends List{

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
    
    return_description(description){
        let str=''
        if (description.length==0){
            str=this.sort_string("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",50)
        }else{
            str=description
        }
        return this.sort_string(str,50)
    }

    return_data(page){
        if (this.array.hasOwnProperty(page)){
            let new_array=this.array[page].Objets;
            for (let serie of new_array){
                let str=''
                str+='<div class="card series-cart">'
                str+='<img src="'+serie.avatar+'" class="card-img-top">'
                str+='<div class="card-body">'
                str+='</div>'
                str+='<h5 class="card-title">'+serie.name+'</h5>'
                str+='<p class="card-text">'+this.return_description(serie.description)+'</p>'
                str+='<a href="'+serie.dir+'/series_id.html" class="btn btn-primary">'+serie.name+'</a>'
                str+='</div>'
                this.div_output.innerHTML+=str
            }
        }
    }
}

class StarsList extends List{

    return_data(page){
        if (this.array.hasOwnProperty(page)){
            let new_array=this.array[page].Objets;
            for (let star of new_array){
                let str='<div class="col col-star">'
                str+='<a href="'+star.dir+'/stars_id.html">'
                str+='<div class="card star-cart">'
                str+='<img src="'+star.avatar+'" class="card-img-top star-cart-img">'
                str+='<div class="card-body">'
                str+=star.name
                str+='</div>'
                str+='</div>'
                str+='</a>'
                str+='</div>'
                this.div_output.innerHTML+=str
            }
        }
    }
}

class ProducentsList extends List{

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

    return_description(description){
        let str=''
        if (description.length==0){
            str=this.sort_string("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",50)
        }else{
            str=description
        }
        return this.sort_string(str,50)
    }

    return_data_filter(filter,array){

        if(filter.hasOwnProperty('name')){
            let value   = filter['name']
            let result=[]
            for (let data of array) {
                let re = new RegExp(value);
                let req_exp = re.test(data.name);
                if (req_exp){
                    result.push(data)
                }
            }
            return result
        }

        if (filter.hasOwnProperty('raiting')){
            let raiting   = filter['raiting']
            let result=[]
            for (let data of array) {
                if (data.rating==raiting){
                    result.push(data)
                }
            }
            return result
        }

        if(filter.hasOwnProperty('series')){
            let value   = filter['series']
            let result=[]
            for (let data of array) {
                if (data['short_series'].name == value){
                    result.push(data)
                }
            }
            return result
        }

        if (filter.hasOwnProperty('tag')){
            let value   = filter['tag']
            let result=[]
            for (let data of array) {
                for (let tag of data['tags']){
                    if (tag.name == value){
                        result.push(data)
                    }
                }
            }
            return result
        } 
    }

    return_data(page){
        if (this.array.hasOwnProperty(page)){
            let new_array=this.array[page].Objets;
            for (let producent of new_array){
                let str=''
                str+='<div class="card series-cart">'
                str+='<img src="'+producent.avatar+'" class="card-img-top">'
                str+='<div class="card-body">'
                str+='</div>'
                str+='<h5 class="card-title">'+producent.name+'</h5>'
                str+='<p class="card-text">'+this.return_description(producent.description)+'</p>'
                str+='<a href="'+producent.dir+'/producent_id.html" class="btn btn-primary">'+producent.name+'</a>'
                str+='</div>'
                this.div_output.innerHTML+=str
            }
        }
    }
}
