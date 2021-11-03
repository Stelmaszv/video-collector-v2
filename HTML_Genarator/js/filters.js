class Form{
    div= ''
    constructor(){
        this.on_init()
        this.form=document.querySelector(this.div)
        console.log(this.form)
    }

    return_form(){
        return this.form.innerHTML=this.html()
    }
}

class FilterMovies extends Form{ 

    on_init(){
        this.div='.movies-filter'
    }

    html(){
        let form ='<input type="text" class="form-control" placeholder="First name" aria-label="First name">'
        return form
        
    }

}
