```
//ENTIDAD LOCALIDAD
package com.persona.Backend.Entity.Parameter.Ubicacion;

import com.persona.Backend.Entity.BaseEntity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "localidad")
public class Localidad extends BaseEntity {

	@Column(name = "nombre", length = 45, nullable = false)
	private String nombre;

	@Column(name = "codigo_postal", length = 45, nullable = false)
	private Integer codigoPostal;

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "ciudad_id", nullable = false, unique = false)
	private Ciudad ciudadId;

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public Integer getCodigoPostal() {
		return codigoPostal;
	}

	public void setCodigoPostal(Integer codigoPostal) {
		this.codigoPostal = codigoPostal;
	}

	public Ciudad getCiudadId() {
		return ciudadId;
	}

	public void setCiudadId(Ciudad ciudadId) {
		this.ciudadId = ciudadId;
	}

}
//IREPOSITORY LOCALIDAD
package com.persona.Backend.IRepository.Parameter.Ubicacion;

import com.persona.Backend.Entity.Parameter.Ubicacion.Localidad;
import com.persona.Backend.IRepository.IBaseRepository;

public interface ILocalidadRepository extends IBaseRepository<Localidad, Long>{

}
//ISERVICE LOCALIDAD
package com.persona.Backend.IService.Parameter.Ubicacion;

import com.persona.Backend.Entity.Parameter.Ubicacion.Localidad;
import com.persona.Backend.IService.IBaseService;

public interface ILocalidadService extends IBaseService<Localidad>{

}
//SERVICE LOCALIDAD
package com.persona.Backend.Service.Parameter.Ubicacion;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Parameter.Ubicacion.Localidad;
import com.persona.Backend.IService.Parameter.Ubicacion.ILocalidadService;
import com.persona.Backend.Service.BaseService;

@Service
public class LocalidadService extends BaseService<Localidad> implements ILocalidadService {

}
//CONTROLLER LOCALIDAD 
package com.persona.Backend.Controller.Parameter.Ubicacion;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Parameter.Ubicacion.Localidad;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/parameter/ubicacion/localidad")
public class LocalidadController extends BaseController<Localidad>{

}




```
