```
//ENTITY CARGO
package com.persona.Backend.Entity.Operational.GestionPersonal;

import com.persona.Backend.Entity.BaseEntity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Table;

@Entity
@Table(name= "cargo")
public class Cargo extends BaseEntity{

	@Column(name = "codigo", length = 45, nullable = false)
	private String codigo;

	@Column(name = "nombre", length = 45, nullable = false)
	private String nombre;

	@Column(name = "descripcion", length = 45, nullable = false)
	private String descripcion;

	public String getCodigo() {
		return codigo;
	}

	public void setCodigo(String codigo) {
		this.codigo = codigo;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getDescripcion() {
		return descripcion;
	}

	public void setDescripcion(String descripcion) {
		this.descripcion = descripcion;
	}
	
	
}
//IREPOSITORY CARGO
package com.persona.Backend.IRepository.Operational.GestionPersonal;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Operational.GestionPersonal.Cargo;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface ICargoRepository extends IBaseRepository<Cargo, Long>{

}
//ISERVICE CARGO
package com.persona.Backend.IService.Operational.GestionPersonal;

import com.persona.Backend.Entity.Operational.GestionPersonal.Cargo;
import com.persona.Backend.IService.IBaseService;

public interface ICargoService extends IBaseService<Cargo>{

}
//SERVICE CARGO
package com.persona.Backend.Service.Operational.GestionPersonal;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Operational.GestionPersonal.Cargo;
import com.persona.Backend.IService.Operational.GestionPersonal.ICargoService;
import com.persona.Backend.Service.BaseService;

@Service
public class CargoService extends BaseService<Cargo> implements ICargoService{

}
//CONTROLLER CARGO
package com.persona.Backend.Controller.Operational.GestionPersonal;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Operational.GestionPersonal.Cargo;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/operational/gestion_personal/cargo")
public class CargoController extends BaseController<Cargo>{

}


```