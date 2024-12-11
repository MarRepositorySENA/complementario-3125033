```
//ENTITY NIVELFORMACION
package com.persona.Backend.Entity.Operational.GestionFormativa;

import com.persona.Backend.Entity.BaseEntity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Table;

@Entity
@Table(name = "nivel_formacion")
public class NivelFormacion extends BaseEntity {
	
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
//IREPOSITORY NIVELFORMACION
package com.persona.Backend.IRepository.Operational.GestionFormativa;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Operational.GestionFormativa.NivelFormacion;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface INivelFormacionRepository extends IBaseRepository<NivelFormacion, Long>{

}
//ISERVICE NIVELFORMACION
package com.persona.Backend.IService.Operational.GestionFormativa;

import com.persona.Backend.Entity.Operational.GestionFormativa.NivelFormacion;
import com.persona.Backend.IService.IBaseService;

public interface INivelFormacionService extends IBaseService<NivelFormacion>{

}
//SERVICE NIVELFORMACION
package com.persona.Backend.Service.Operational.GestionFormativa;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Operational.GestionFormativa.NivelFormacion;
import com.persona.Backend.IService.Operational.GestionFormativa.INivelFormacionService;
import com.persona.Backend.Service.BaseService;

@Service
public class NivelFormacioService extends BaseService<NivelFormacion> implements INivelFormacionService{

}
//CONTROLLER NIVELFORMACION
package com.persona.Backend.Controller.Operational.GestionFormativa;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Operational.GestionFormativa.NivelFormacion;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/operational/gestion_formativa/nivel_formacion")
public class NivelFormacionController extends BaseController<NivelFormacion> {

}


```