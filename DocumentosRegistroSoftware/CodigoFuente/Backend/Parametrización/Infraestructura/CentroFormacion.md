```
//ENTITY AMBIENTE
package com.persona.Backend.Entity.Parameter.Infraestrutura;

import com.persona.Backend.Entity.BaseEntity;
import com.persona.Backend.Entity.Parameter.Ubicacion.Ciudad;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "centro_formacion")
public class CentroFormacion extends BaseEntity {


	@Column(name = "nombre", length = 45, nullable = false)
	private String nombre;

	@Column(name = "codigo", length = 10, nullable = false)
	private String codigo;

	@Column(name = "direccion", length = 45, nullable = false)
	private String direccion;

	@Column(name = "telefono", length = 15, nullable = false)
	private String telefono;

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "regional_id", nullable = false, unique = false)
	private Regional regionalId;

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "cuidad_id", nullable = false, unique = false)
	private Ciudad ciudadId;

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getCodigo() {
		return codigo;
	}

	public void setCodigo(String codigo) {
		this.codigo = codigo;
	}

	public String getDireccion() {
		return direccion;
	}

	public void setDireccion(String direccion) {
		this.direccion = direccion;
	}

	public String getTelefono() {
		return telefono;
	}

	public void setTelefono(String telefono) {
		this.telefono = telefono;
	}

	public Regional getRegionalId() {
		return regionalId;
	}

	public void setRegionalId(Regional regionalId) {
		this.regionalId = regionalId;
	}

	public Ciudad getCiudadId() {
		return ciudadId;
	}

	public void setCiudadId(Ciudad ciudadId) {
		this.ciudadId = ciudadId;
	}

}
//IREPOSITORY CENTROFORMACION
package com.persona.Backend.IRepository.Parameter.Infraestructura;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Parameter.Infraestrutura.CentroFormacion;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface ICentroFormacionRepository extends IBaseRepository<CentroFormacion, Long> {

}
ISERVICE CENTROFORMACION
package com.persona.Backend.IService.Parameter.Infraestructura;

import com.persona.Backend.Entity.Parameter.Infraestrutura.CentroFormacion;
import com.persona.Backend.IService.IBaseService;

public interface ICentroFormacionService extends IBaseService<CentroFormacion>{

}
//SERVICE CENTROFORMACION
package com.persona.Backend.Service.Parameter.Infraestructura;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Parameter.Infraestrutura.CentroFormacion;
import com.persona.Backend.IService.Parameter.Infraestructura.ICentroFormacionService;
import com.persona.Backend.Service.BaseService;

@Service
public class CentroFormacionService extends BaseService<CentroFormacion> implements ICentroFormacionService{

}
//CONTROLLER CENTROFORMACION 
package com.persona.Backend.Controller.Parameter.Infraestructura;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Parameter.Infraestrutura.CentroFormacion;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/parameter/infraestructura/centro_formacion")
public class CentroFormacionController extends BaseController<CentroFormacion> {

}


```
