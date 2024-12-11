```
//ENTITY SEDE
package com.persona.Backend.Entity.Parameter.Infraestrutura;

import com.persona.Backend.Entity.BaseEntity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "sede")
public class Sede extends BaseEntity {

	@Column(name = "codigo", length = 45, nullable = false)
	private String codigo;

	@Column(name = "nombre", length = 45, nullable = false)
	private String nombre;

	@Column(name = "direccion", length = 45, nullable = false)
	private String direccion;

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "centro_formacion_id", nullable = false, unique = false)
	private CentroFormacion centroFormacionId;

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

	public String getDireccion() {
		return direccion;
	}

	public void setDireccion(String direccion) {
		this.direccion = direccion;
	}

	public CentroFormacion getCentroFormacionId() {
		return centroFormacionId;
	}

	public void setCentroFormacionId(CentroFormacion centroFormacionId) {
		this.centroFormacionId = centroFormacionId;
	}

}
//IREPOSITORY SEDE
package com.persona.Backend.IRepository.Parameter.Infraestructura;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Parameter.Infraestrutura.Sede;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface ISedeRepository extends IBaseRepository<Sede, Long>{

}
//ISERVICE SEDE
package com.persona.Backend.IService.Parameter.Infraestructura;

import com.persona.Backend.Entity.Parameter.Infraestrutura.Sede;
import com.persona.Backend.IService.IBaseService;

public interface ISedeService extends IBaseService<Sede>{

}
//SERVICE SEDE
package com.persona.Backend.Service.Parameter.Infraestructura;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Parameter.Infraestrutura.Sede;
import com.persona.Backend.IService.Parameter.Infraestructura.ISedeService;
import com.persona.Backend.Service.BaseService;

@Service
public class SedeService extends BaseService<Sede> implements ISedeService {

}
//CONTROLLER SEDE
package com.persona.Backend.Controller.Parameter.Infraestructura;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Parameter.Infraestrutura.Sede;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/parameter/infraestructura/sede")
public class SedeController extends BaseController<Sede> {

}


```