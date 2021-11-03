let page=0
class LoadContet{

    constructor(filter=[]){
        this.set_data()
        this.set_list()
        let div_output=document.querySelector(this.div_output)
        div_output.innerHTML=''
        this.ListOBJ = this.set_obj()
        this.ListOBJ.return_data(page)
        if (this.filter_is_not_empty(filter)){
            page=0
            div_output.innerHTML=''
            this.ListOBJ.return_data_filter(filter,this.data)
            this.data=this.ListOBJ.array
            this.set_list()
            this.ListOBJ = this.set_obj()
            this.ListOBJ.return_data(page)
            //console.log(this)
            //console.log(this.ListOBJ)
            //this.ListOBJ.return_data(page)
            /*
            this.set_list()
            this.ListOBJ = this.set_obj()
            console.log(this.ListOBJ.array)
            this.ListOBJ.return_data(page)
            */
        }
    
        page++
    }

    filter_is_not_empty(filter){
        return filter.hasOwnProperty('name')
    }

    set_list(){
        const PaginatorMovies = new Paginator(this.data,this.limit)
        this.pagineted_data=PaginatorMovies.genrate_pages()
    }
}

class LoadMovies extends LoadContet{

    set_obj(){
        return new MovieList(this.div_output,this.pagineted_data)
    }

    set_data(data=[]){
        this.div_output='.movies-output'
        this.data=movies
        this.limit=20
    }
}

class LoadSeries extends LoadContet{

    set_obj(){
        return new SeriesList(this.div_output,this.pagineted_data)
    }

    set_data(){
        this.div_output='.series-output'
        this.data=series
        this.limit=5
    }
}

class LoadStars extends LoadContet{

    set_obj(){
        return new StarsList(this.div_output,this.pagineted_data)
    }

    set_data(){
        this.div_output='.stars-otput'
        this.data=stars
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
        this.limit=15
    }
}