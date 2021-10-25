class Search{

    search='.search'
    results='.results'

    construct(){
        this.on_key_up(this)
    }

    on_key_up(Obj){
        let search  = document.querySelector(this.search)
        let results = document.querySelector(this.results)
        search.addEventListener("keyup", function(){
            results.innerHTML=""
            let length=Obj.data.length
            let value=search.value
            if (value.length>2){
                for (let page = 0; page < length; page++) {
                    for (let objetc of Obj.data[page]['Objets']){
                        let re = new RegExp(value);
                        let req_exp = re.test(objetc.name);
                        if (req_exp){
                            Obj.on_result(results,objetc)
                        }
                    }
                }
            }else{
                results.innerHTML="Min 3 leters"
            }
        });
    }
}

class StarsSearch extends Search{
    data=stars
    on_result(results,objetc){
        results.innerHTML+= '<div class="el"><a href="'+objetc.dir+'/stars_id.html">'+objetc.show_name+'</a><div>';
    }
}

class SeriesSearch extends Search{
    data=series
    on_result(results,objetc){
        results.innerHTML+= '<div class="el"><a href="'+objetc.dir+'/series_id.html">'+objetc.show_name+'</a><div>';
    }
}

class MoviesSearch extends Search{
    data=movies
    on_result(results,objetc){
        results.innerHTML+= '<div class="el"><a href="'+objetc.dir+'/movies_id.html">'+objetc.show_name+'</a><div>';
    }
}

class ProducentSearch extends Search{
    data=producents
    on_result(results,objetc){
        results.innerHTML+= '<div class="el"><a href="'+objetc.dir+'/producent_id.html">'+objetc.show_name+'</a><div>';
    }
}

class SetSearch{
    wheresearch='.where-search'
    startsearch='.search'
    construct(){
        this.on_search(this)
    }
    on_search(Obj){
        this.where=document.querySelector(this.wheresearch)
        this.where.addEventListener("change", function(){
            let start=document.querySelector(Obj.startsearch)
            let where_value=this.value
            if (where_value!==''){
                start.disabled=false
                Obj.set_data(where_value)
            }else{
                start.disabled=true
            }
        });
    }

    set_data(set_data){
        const objets={
            "Producents"  : new ProducentSearch(),
            "Movies"      : new MoviesSearch(),
            "Series"      : new SeriesSearch(),
            "Stars"       : new StarsSearch(),
        }
        objets[set_data].construct()
    }
}