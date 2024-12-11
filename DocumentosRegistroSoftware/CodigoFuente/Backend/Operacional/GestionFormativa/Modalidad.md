```
//ENTITY MODALIDAD
package com.persona.Backend.Entity.Operational.GestionFormativa;

import com.persona.Backend.Entity.BaseEntity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Table;

@Entity
@Table(name=" modalidad")
public class Modalidad extends BaseEntity{
	
	@Column(name = "codigo", length = 45, nullable = false)
	private String codigo;

	@Column(name = "nombre", length = 45, nullable = false)
	private String nombre;
	
	@Column(name = "descripcion", length = 45, nullable = false)
	private String descripcion;
	
	@Column(name = "requiere_presencialidad", length = 45, nullable = false)
	private Boolean requierePresencialidad;

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

	public Boolean getRequierePresencialidad() {
		return requierePresencialidad;
	}

	public void setRequierePresencialidad(Boolean requierePresencialidad) {
		this.requierePresencialidad = requierePresencialidad;
	}

}
//IREPOSITORY MODALIDAD
package com.persona.Backend.IRepository.Operational.GestionFormativa;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Operational.GestionFormativa.Modalidad;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface IModalidadRepository extends IBaseRepository<Modalidad, Long>{

}
//ISERVICE MODALIDAD
package com.persona.Backend.IService.Operational.GestionFormativa;

import com.persona.Backend.Entity.Operational.GestionFormativa.Modalidad;
import com.persona.Backend.IService.IBaseService;

public interface IModalidadService extends IBaseService<Modalidad> {

}
//SERVICE MODALIDAD
package com.persona.Backend.Service.Operational.GestionFormativa;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Operational.GestionFormativa.Modalidad;
import com.persona.Backend.IService.Operational.GestionFormativa.IModalidadService;
import com.persona.Backend.Service.BaseService;

@Service
public class ModalidadService extends BaseService<Modalidad> implements IModalidadService{

}
//CONTROLLER MODALIDAD
package com.persona.Backend.Controller.Operational.GestionFormativa;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Operational.GestionFormativa.Modalidad;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/operational/gestion_formativa/modalidad")
public class ModalidadController extends BaseController<Modalidad>{

}



```